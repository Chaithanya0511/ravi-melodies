# from rest_framework.test import APITestCase
# import os
# from voice.models import (
#     TodaysPerformance, AboutEventsSchedule, Meet_our_teame, Event, EventPhoto, EventVideo,
#     DomesticEvent, DomesticEventPhoto, DomesticEventVideo, Meet_our_clients, ContactFormSubmission, EmailSubmission, RecentHighlight
# )
# from voice.serializer import (
#     TodaysPerformanceSerializer, about_events_scheduleSerializer, EventSerializer,
#     EventPhotoSerializer, EventVideoSerializer, DomesticEventSerializer,
#     DomesticEventPhotoSerializer, DomesticEventVideoSerializer, aboutus_Serializer,
#     Meet_our_clients_serializer,RecentSerializer
# )


# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status

 
# class RecentHighlightTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.event = Event.objects.create(title="Global Conference", date="2023-10-01")
#         self.domestic_event = DomesticEvent.objects.create(title="Local Meetup", date="2023-10-05")
#         self.highlight_with_event = RecentHighlight.objects.create(
#             event_type="event",
#             event=self.event,
#             video_clip="recent_highlight_videos/global_conference.mp4"
#         )
#         self.highlight_with_domestic_event = RecentHighlight.objects.create(
#             event_type="domestic_event",
#             domestic_event=self.domestic_event,
#             video_clip="recent_highlight_videos/local_meetup.mp4"
#         )
 
#     def test_recent_highlight_creation(self):
#         """Test that a RecentHighlight instance is created correctly."""
#         self.assertEqual(self.highlight_with_event.event_type, "event")
#         self.assertEqual(self.highlight_with_event.event.title, "Global Conference")
#         self.assertEqual(self.highlight_with_domestic_event.event_type, "domestic_event")
#         self.assertEqual(self.highlight_with_domestic_event.domestic_event.title, "Local Meetup")
 
#     def test_recent_serializer_with_event(self):
#         """Test the RecentSerializer with an event."""
#         serializer = RecentSerializer(self.highlight_with_event)
#         expected_data = {
#             'id': self.highlight_with_event.id,
#             'event_type': 'event',
#             'event': self.event.id,
#             'domestic_event': None,
#             'video_clip': '/media/recent_highlight_videos/global_conference.mp4'
#         }
#         self.assertEqual(serializer.data, expected_data)
 
#     def test_recent_serializer_with_domestic_event(self):
#         """Test the RecentSerializer with a domestic event."""
#         serializer = RecentSerializer(self.highlight_with_domestic_event)
#         expected_data = {
#             'id': self.highlight_with_domestic_event.id,
#             'event_type': 'domestic_event',
#             'event': None,
#             'domestic_event': self.domestic_event.id,
#             'video_clip': '/media/recent_highlight_videos/local_meetup.mp4'
#         }
#         self.assertEqual(serializer.data, expected_data)
 
#     def test_recent_api_get(self):
#         """Test the GET request to the Recent_api view."""
#         url = "/api_recent/"
#         response = self.client.get(url)
#         highlights = RecentHighlight.objects.all()
#         serializer = RecentSerializer(highlights, many=True)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)
 
#     def test_recent_api_get_with_event_filter(self):
#         """Test the GET request to the Recent_api view with an event filter."""
#         url = f"/api_recent/?event={self.event.id}"
#         response = self.client.get(url)
#         highlights = RecentHighlight.objects.all()  # View returns all highlights
#         serializer = RecentSerializer(highlights, many=True)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)
 
#     def test_recent_api_get_with_domestic_event_filter(self):
#         """Test the GET request to the Recent_api view with a domestic event filter."""
#         url = f"/api_recent/?domestic_event={self.domestic_event.id}"
#         response = self.client.get(url)
#         highlights = RecentHighlight.objects.all()  # View returns all highlights
#         serializer = RecentSerializer(highlights, many=True)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)
 


# class SerializerTestCase(APITestCase):
    
#     def test_todays_performance_serializer(self):
#         performance = TodaysPerformance.objects.create(singers_name="John Doe", profession="Singer", twitter_url="https://twitter.com/johndoe", facebook_url="https://facebook.com/johndoe", instagram_url="https://instagram.com/johndoe")
#         serializer = TodaysPerformanceSerializer(performance)
#         self.assertEqual(serializer.data['singers_name'], "John Doe")

#     def test_about_events_schedule_serializer(self):
#         event_schedule = AboutEventsSchedule.objects.create(title_event="Annual Event", place_event="New York", date_time="2025-03-19T10:00:00Z", description="A great event.", right_left="right")
#         serializer = about_events_scheduleSerializer(event_schedule)
#         self.assertEqual(serializer.data['title_event'], "Annual Event")

#     def test_event_serializer(self):
#         event = Event.objects.create(name="Music Fest", place="New York", title="Music Festival", description="Annual music festival.", location="NYC Central Park", cover_image="event.jpg")
#         serializer = EventSerializer(event)
#         self.assertEqual(serializer.data['name'], "Music Fest")

#     def test_event_photo_serializer(self):
#         event = Event.objects.create(name="Concert", place="NYC", title="Live Concert", description="Amazing live concert.", location="Madison Square Garden", cover_image="concert.jpg")
#         photo = EventPhoto.objects.create(event=event, image="event_photos/test.jpg")
#         serializer = EventPhotoSerializer(photo)
#         self.assertTrue(serializer.data['image'].endswith("test.jpg"))
    
#     def test_event_video_serializer(self):
#         event = Event.objects.create(name="Concert", place="NYC", title="Live Concert", description="Amazing live concert.", location="Madison Square Garden", cover_image="concert.jpg")
#         video = EventVideo.objects.create(event=event, video="event_videos/test.mp4")
#         serializer = EventVideoSerializer(video)
#         self.assertTrue(serializer.data['video'].endswith("test.mp4"))

#     def test_domestic_event_serializer(self):
#         domestic_event = DomesticEvent.objects.create(name="Cultural Fest", place="Hyderabad", title="Cultural Festival", description="Annual cultural festival.", location="City Hall", cover_image="cultural.jpg")
#         serializer = DomesticEventSerializer(domestic_event)
#         self.assertEqual(serializer.data['name'], "Cultural Fest")

#     def test_domestic_event_photo_serializer(self):
#         domestic_event = DomesticEvent.objects.create(name="Cultural Fest", place="Hyderabad", title="Cultural Festival", description="Annual cultural festival.", location="City Hall", cover_image="cultural.jpg")
#         domestic_photo = DomesticEventPhoto.objects.create(event=domestic_event, image="domestic_event_photos/domestic.jpg")
#         serializer = DomesticEventPhotoSerializer(domestic_photo)
#         self.assertTrue(serializer.data['image'].endswith("domestic.jpg"))

#     def test_domestic_event_video_serializer(self):
#         domestic_event = DomesticEvent.objects.create(name="Cultural Fest", place="Hyderabad", title="Cultural Festival", description="Annual cultural festival.", location="City Hall", cover_image="cultural.jpg")
#         domestic_video = DomesticEventVideo.objects.create(event=domestic_event, video="domestic_event_videos/domestic.mp4")
#         serializer = DomesticEventVideoSerializer(domestic_video)
#         self.assertTrue(serializer.data['video'].endswith("domestic.mp4"))
    
#     def test_meet_our_team_serializer(self):
#         team_member = Meet_our_teame.objects.create(name="Alice", profession="Manager", image="alice.jpg", twitter_url="https://twitter.com/alice", facebook_url="https://facebook.com/alice", instagram_url="https://instagram.com/alice")
#         serializer = aboutus_Serializer(team_member)
#         self.assertEqual(serializer.data['name'], "Alice")
    
#     def test_meet_our_clients_serializer(self):
#         client = Meet_our_clients.objects.create(company_name="XYZ Corp", image="xyz.jpg")
#         serializer = Meet_our_clients_serializer(client)
#         self.assertEqual(serializer.data['company_name'], "XYZ Corp")
