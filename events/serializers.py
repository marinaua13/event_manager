from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event, EventRegistration


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')
    registrations_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__' + ['registrations_count']

    def get_registrations_count(self, obj):
        return obj.registrations.count()


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRegistration
        fields = ['id', 'event', 'user', 'registered_at']
        read_only_fields = ['user', 'registered_at']
