# from django.test import TestCase
# from voice.models import *
# from django.core.exceptions import ValidationError
# from django.utils.timezone import now
# from io import BytesIO
# from django.core.files.uploadedfile import SimpleUploadedFile

# import datetime

# class RecentHighlightModelTest(TestCase):
#     def setUp(self):
#         """Set up test data before each test"""
#         self.event = Event.objects.create(
#             name="Test Event",
#             place="Test Place",
#             eimage="test_image.jpg",
#             title="Test Event Title",
#             description="Test event description",
#             date=datetime.date(2025, 3, 20),
#             time=datetime.time(14, 30),
#             location="Test Location",
#             cover_image="test_cover.jpg"
#         )

#         self.domestic_event = DomesticEvent.objects.create(
#             name="Test Domestic Event",
#             place="Test Domestic Place",
#             eimage="test_domestic_image.jpg",
#             title="Test Domestic Event Title",
#             description="Test domestic event description",
#             date=datetime.date(2025, 3, 21),
#             time=datetime.time(16, 45),
#             location="Test Domestic Location",
#             cover_image="test_domestic_cover.jpg"
#         )

#     def test_valid_recent_highlight_event(self):
#         """Test creating a valid RecentHighlight with an Event"""
#         highlight = RecentHighlight.objects.create(
#             event=self.event,
#             video_clip="videos/test_video.mp4",
#             event_type="event"
#         )
#         self.assertIsNotNone(highlight.pk)  # Ensure object is saved successfully

#     def test_valid_recent_highlight_domestic_event(self):
#         """Test creating a valid RecentHighlight with a DomesticEvent"""
#         highlight = RecentHighlight.objects.create(
#             domestic_event=self.domestic_event,
#             video_clip="videos/test_domestic_video.mp4",
#             event_type="domestic_event"
#         )
#         self.assertIsNotNone(highlight.pk)  # Ensure object is saved successfully

#     def test_invalid_recent_highlight_both_selected(self):
#         """Test validation error when both Event and DomesticEvent are selected"""
#         highlight = RecentHighlight(
#             event=self.event,
#             domestic_event=self.domestic_event,
#             video_clip="videos/test_video.mp4",
#             event_type="event"
#         )
#         with self.assertRaises(ValidationError) as e:
#             highlight.full_clean()  # Run model validation manually
#         self.assertIn("You cannot select both Event and Domestic Event", str(e.exception))

#     def test_invalid_recent_highlight_none_selected(self):
#         """Test validation error when neither Event nor DomesticEvent is selected"""
#         highlight = RecentHighlight(
#             video_clip="videos/test_video.mp4",
#             event_type="event"
#         )
#         with self.assertRaises(ValidationError) as e:
#             highlight.full_clean()
#         self.assertIn("You must select either an Event or a Domestic Event", str(e.exception))


# class ModelsTestCase(TestCase):
#     def setUp(self):

#         # Sample Image
#         self.image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
    
#         # Sample Video
#         self.video = SimpleUploadedFile(name='test_video.mp4', content=b'', content_type='video/mp4')
    
#         # Creating an Event
#         self.event = Event.objects.create(
#             name="Music Concert",
#             place="Hyderabad",
#             eimage=self.image,
#             title="Grand Music Night",
#             description="A night full of music and joy",
#             date=now().date(),
#             location="City Auditorium",
#              cover_image=self.image
#         )

        
#         # Creating Domestic Event
#         self.domestic_event = DomesticEvent.objects.create(
#             name="Wedding Event",
#             place="Delhi",
#             eimage=self.image,
#             title="Wedding Special",
#             description="Traditional wedding event",
#             date=now().date(),
#             location="Banquet Hall",
#             cover_image=self.image
#         )
        
#     def test_event_creation(self):
#         event = Event.objects.get(title="Grand Music Night")
#         self.assertEqual(event.name, "Music Concert")
#         self.assertEqual(event.place, "Hyderabad")
        
#     def test_domestic_event_creation(self):
#         domestic_event = DomesticEvent.objects.get(title="Wedding Special")
#         self.assertEqual(domestic_event.name, "Wedding Event")
#         self.assertEqual(domestic_event.place, "Delhi")
        
#     def test_event_video_upload(self):
#         event_video = EventVideo.objects.create(event=self.event, video=self.video)
#         self.assertTrue(event_video.video.name.endswith('.mp4'))
        
#     def test_meet_our_team_validation(self):
#         team_member = Meet_our_teame(
#             name="John Doe",
#             profession="Singer",
#             image=SimpleUploadedFile(name='profile.jpg', content=b'', content_type='image/jpeg'),
#             twitter_url="https://twitter.com/johndoe",
#             facebook_url="https://facebook.com/johndoe",
#             instagram_url="https://instagram.com/johndoe"
#         )
#         team_member.full_clean()  # Ensure validation passes
#         team_member.save()
        
#         self.assertEqual(team_member.name, "John Doe")
        
#     def test_invalid_profession(self):
#         team_member = Meet_our_teame(
#             name="Invalid User",
#             profession="Singer123",
#             image=SimpleUploadedFile(name='profile.jpg', content=b'', content_type='image/jpeg'),
#             twitter_url="https://twitter.com/user",
#             facebook_url="https://facebook.com/user",
#             instagram_url="https://instagram.com/user"
#         )
#         with self.assertRaises(ValidationError):
#             team_member.full_clean()
    
#     def test_email_submission(self):
#         valid_email = EmailSubmission(email="test@example.com")
#         valid_email.full_clean()  # Ensures validation passes
#         valid_email.save()
        
#         with self.assertRaises(ValidationError):
#             invalid_email = EmailSubmission(email="invalid-email")
#             invalid_email.full_clean()
    
#     def test_contact_form_submission(self):
#         contact = ContactFormSubmission.objects.create(
#             first_name="Jane",
#             last_name="Doe",
#             email="jane.doe@example.com",
#             mobile="9876543210",
#             message="Hello! I am interested in your events."
#         )
#         self.assertEqual(contact.first_name, "Jane")
#         self.assertEqual(contact.last_name, "Doe")
#         self.assertEqual(contact.email, "jane.doe@example.com")