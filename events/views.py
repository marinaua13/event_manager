from django.contrib.auth.models import User

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Event, EventRegistration
from .serializers import EventSerializer, UserSerializer
from .filters import EventFilter


def send_registration_email(user, event):
    subject = f"Registration Confirmed: {event.title}"
    from_email = 'noreply@eventapp.com'
    to_email = [user.email]
    context = {'user': user, 'event': event}
    text_content = f"You have registered for {event.title}."
    html_content = render_to_string('emails/registration_email.html', context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    print(f"✅ Email sent to {user.email} for event: {event.title}")


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.select_related('organizer').prefetch_related('registrations')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = EventFilter

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def register(self, request, pk=None):
        event = self.get_object()
        user = request.user
        registration, created = EventRegistration.objects.get_or_create(event=event, user=user)
        if not created:
            return Response({'detail': 'Already registered'}, status=400)
        send_registration_email(user, event)
        return Response({'detail': 'Registered successfully'})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.prefetch_related('event_registrations').all()
    serializer_class = UserSerializer
