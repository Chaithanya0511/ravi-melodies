
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from voice.models import (
    TodaysPerformance, AboutEventsSchedule, Meet_our_teame, Event,
    EventPhoto, EventVideo, DomesticEvent, DomesticEventPhoto,
    DomesticEventVideo, Meet_our_clients,RecentHighlight
)
from voice.serializer import (
    TodaysPerformanceSerializer, about_events_scheduleSerializer,
    aboutus_Serializer, EventSerializer, DomesticEventSerializer,
    Dphoto, Dvideo, Meet_our_clients_serializer,RecentSerializer  # Removed 'Iphoto'
)

from django.test import TestCase



 
class RecentHighlightAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.event = Event.objects.create(title="Global Conference", date="2023-10-01")
        self.domestic_event = DomesticEvent.objects.create(title="Local Meetup", date="2023-10-05")
        self.highlight_with_event = RecentHighlight.objects.create(
            event_type="event",
            event=self.event,
            video_clip="recent_highlight_videos/global_conference.mp4"
        )
        self.highlight_with_domestic_event = RecentHighlight.objects.create(
            event_type="domestic_event",
            domestic_event=self.domestic_event,
            video_clip="recent_highlight_videos/local_meetup.mp4"
        )
 
    def test_get_all_highlights(self):
        """Test that the API returns all RecentHighlight objects."""
        url = "/api_recent/"
        response = self.client.get(url)
        highlights = RecentHighlight.objects.all()
        serializer = RecentSerializer(highlights, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
 
    def test_get_highlights_with_event_query_param(self):
        """Test that the API ignores the 'event' query parameter and returns all highlights."""
        url = f"/api_recent/?event={self.event.id}"
        response = self.client.get(url)
        highlights = RecentHighlight.objects.all()  # View returns all highlights
        serializer = RecentSerializer(highlights, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
 
    def test_get_highlights_with_domestic_event_query_param(self):
        """Test that the API ignores the 'domestic_event' query parameter and returns all highlights."""
        url = f"/api_recent/?domestic_event={self.domestic_event.id}"
        response = self.client.get(url)
        highlights = RecentHighlight.objects.all()  # View returns all highlights
        serializer = RecentSerializer(highlights, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
 
    def test_get_highlights_with_invalid_query_param(self):
        """Test that the API ignores invalid query parameters and returns all highlights."""
        url = "/api_recent/?invalid_param=123"
        response = self.client.get(url)
        highlights = RecentHighlight.objects.all()  # View returns all highlights
        serializer = RecentSerializer(highlights, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
 
    def test_get_highlights_empty_database(self):
        """Test that the API returns an empty list when no highlights exist."""
        RecentHighlight.objects.all().delete()  # Delete all highlights
        url = "/api_recent/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
 
 
class TestAPIViews(APITestCase):
    def setUp(self):
        self.client = APIClient()
       
        # Create test data for each model
        self.performance = TodaysPerformance.objects.create(
            upload_image="images/test_image.jpg",
            singers_name="Test Singer",
            profession="Singer",
            twitter_url="https://twitter.com/test",
            facebook_url="https://facebook.com/test",
            instagram_url="https://instagram.com/test"
        )
        self.schedule = AboutEventsSchedule.objects.create(
            date_time="2023-10-01T12:00:00Z",
            upload_image="Eventsimages/test_event_image.jpg",
            title_event="Test Event",
            place_event="Test Place",
            description="Test Description",
            right_left="right"
        )
        self.team_member = Meet_our_teame.objects.create(
            name="Test Team Member",
            profession="Musician",
            image="meetorteam/test_team_image.jpg",
            twitter_url="https://twitter.com/test",
            facebook_url="https://facebook.com/test",
            instagram_url="https://instagram.com/test"
        )
        self.event = Event.objects.create(
            name="Test Event",
            place="Test Place",
            eimage="voice/test_event_image.jpg",
            title="Test Event Title",
            description="Test Event Description",
            date="2023-10-01",
            location="Test Location",
            cover_image="event_covers/test_cover_image.jpg"
        )
        self.event_photo = EventPhoto.objects.create(
            event=self.event,
            image="event_photos/test_photo.jpg"
        )
        self.event_video = EventVideo.objects.create(
            event=self.event,
            video="event_videos/test_video.mp4"
        )
        self.domestic_event = DomesticEvent.objects.create(
            name="Test Domestic Event",
            place="Test Domestic Place",
            eimage="domestic_voice/test_domestic_image.jpg",
            title="Test Domestic Event Title",
            description="Test Domestic Event Description",
            date="2023-10-01",
            location="Test Domestic Location",
            cover_image="domestic_event_covers/test_domestic_cover.jpg"
        )
        self.domestic_photo = DomesticEventPhoto.objects.create(
            event=self.domestic_event,
            image="domestic_event_photos/test_domestic_photo.jpg"
        )
        self.domestic_video = DomesticEventVideo.objects.create(
            event=self.domestic_event,
            video="domestic_event_videos/test_domestic_video.mp4"
        )
        self.client_member = Meet_our_clients.objects.create(
            image="meetourclients/test_client_image.jpg",
            company_name="Test Client Company"
    )
    # def test_todays_performance_api(self):
    #     url = reverse('api_home')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     serializer = TodaysPerformanceSerializer([self.performance], many=True)
    #     self.assertEqual(response.data, serializer.data)
    def test_todays_performance_api(self):
        url = reverse('api_home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = TodaysPerformanceSerializer([self.performance], many=True)
        self.assertEqual(response.data, serializer.data)
 
    def test_about_events_schedule_api(self):
        url = '/api_home1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = about_events_scheduleSerializer([self.schedule], many=True)
        self.assertEqual(response.data, serializer.data)
 
    def test_aboutus_api(self):
        url = '/api_aboutus/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = aboutus_Serializer([self.team_member], many=True)
        self.assertEqual(response.data, serializer.data)
 
    def test_aboutus_clients_api(self):
        url = '/api_clients/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = Meet_our_clients_serializer([self.client_member], many=True)
        self.assertEqual(response.data, serializer.data)
 
    def test_get_events(self):
        url = reverse('get_events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = EventSerializer([self.event], many=True)
        self.assertEqual(response.data, serializer.data)
 
    def test_get_event_detail(self):
        url = reverse('get_event_detail', args=[self.event.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = EventSerializer(self.event)
        self.assertEqual(response.data, serializer.data)
 
    def test_get_event_detail_not_found(self):
        url = reverse('get_event_detail', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
 
    def test_get_domestic_events(self):
        url = reverse('get_domestic_events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = DomesticEventSerializer([self.domestic_event], many=True)
        self.assertEqual(response.data, serializer.data)
 
    def test_get_domestic_event_detail(self):
        url = reverse('get_domestic_event_detail', args=[self.domestic_event.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = DomesticEventSerializer(self.domestic_event)
        self.assertEqual(response.data, serializer.data)
 
    def test_get_domestic_event_detail_not_found(self):
        url = reverse('get_domestic_event_detail', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
 
 
 
 