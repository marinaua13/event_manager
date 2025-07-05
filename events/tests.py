from rest_framework.test import APITestCase
from rest_framework import status
from events.models import Event
from django.contrib.auth import get_user_model


class EventApiTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass123", email="test@example.com"
        )
        self.event = Event.objects.create(
            title="Test Event",
            description="Test Description",
            date="2030-01-01T12:00:00Z",
            location="Test Location",
            organizer=self.user,
        )

    def test_list_events(self):
        url = '/api/events/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Event")
