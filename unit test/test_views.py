# # from django.test import TestCase
# # from django.urls import reverse
# # from voice.views import *

# # class ViewTestCase(TestCase):
# #     def test_home_view(self):
# #         """Test the home view."""
# #         url = reverse('home')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'home.html')

# #     def test_international_view(self):
# #         """Test the international view."""
# #         url = reverse('international')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'international.html')

# #     def test_ivp_view(self):
# #         """Test the ivp view with event_id."""
# #         event_id = 1
# #         url = reverse('ivp', kwargs={'event_id': event_id})
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'ivp.html')
# #         self.assertIn('event_id', response.context)
# #         self.assertEqual(response.context['event_id'], event_id)

# #     def test_domestic_view(self):
# #         """Test the domestic view."""
# #         url = reverse('domestic')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'domestic.html')

# #     def test_dvp_view(self):
# #         """Test the dvp view with event_id."""
# #         event_id = 2
# #         url = reverse('dvp', kwargs={'event_id': event_id})
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'dvp.html')
# #         self.assertIn('event_id', response.context)
# #         self.assertEqual(response.context['event_id'], event_id)

# #     def test_latest_updates_view(self):
# #         """Test the latest_updates view."""
# #         url = reverse('latest_updates')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'latest.html')

# #     def test_tickets_view(self):
# #         """Test the tickets view with event_id."""
# #         event_id = 3
# #         url = reverse('tickets', kwargs={'event_id': event_id})
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'tickets.html')
# #         self.assertIn('event_id', response.context)
# #         self.assertEqual(response.context['event_id'], event_id)

# #     def test_gold_view(self):
# #         """Test the gold view."""
# #         url = reverse('gold')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'gold.html')

# #     def test_silver_view(self):
# #         """Test the silver view."""
# #         url = reverse('silver')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'silver.html')

# #     def test_bronze_view(self):
# #         """Test the bronze view."""
# #         url = reverse('bronze')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'bronze.html')

# #     def test_contact_us_view(self):
# #         """Test the contact_us view."""
# #         url = reverse('contact_us')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'contact.html')

# #     def test_about_us_view(self):
# #         """Test the about_us view."""
# #         url = reverse('about_us')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'about.html')

# #     def test_gallery_view(self):
# #         """Test the gallery view."""
# #         url = reverse('gallery')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'gallery.html')

# #     def test_gallery_videos_view(self):
# #         """Test the gallery_videos view."""
# #         url = reverse('gallery_videos')
# #         response = self.client.get(url)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'gallery_videos.html')



# from django.test import TestCase, Client
# from django.urls import reverse
# from voice.models import ContactFormSubmission, EmailSubmission,Event, DomesticEvent, RecentHighlight
# import datetime

# class RecentHighlightViewTest(TestCase):
#     def setUp(self):
#         """Set up test data before each test"""
#         self.client = Client()  # Django test client

#         # Create an Event
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

#         # Create a Domestic Event
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

#         # Create RecentHighlight for event
#         self.highlight1 = RecentHighlight.objects.create(
#             event=self.event,
#             video_clip="videos/test_video.mp4",
#             event_type="event"
#         )

#         # Create RecentHighlight for domestic event
#         self.highlight2 = RecentHighlight.objects.create(
#             domestic_event=self.domestic_event,
#             video_clip="videos/test_domestic_video.mp4",
#             event_type="domestic_event"
#         )

#     def test_recent_view_status_code(self):
#         """Test if the recent view returns a 200 status code"""
#         response = self.client.get(reverse("recent"))  # Replace with your actual URL name
#         self.assertEqual(response.status_code, 200)

#     def test_recent_view_template_used(self):
#         """Test if the correct template is used"""
#         response = self.client.get(reverse("recent"))
#         self.assertTemplateUsed(response, "recent.html")

#     def test_recent_view_context_data(self):
#         """Test if the recent view passes the correct highlights data"""
#         response = self.client.get(reverse("recent"))
#         self.assertTrue("highlights" in response.context)  # Check if highlights exist in context
#         self.assertEqual(len(response.context["highlights"]), 2)  # Ensure 2 highlights are passed
#         self.assertIn(self.highlight1, response.context["highlights"])  # Check event highlight
#         self.assertIn(self.highlight2, response.context["highlights"])  # Check domestic event highlight


# class ViewsTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.valid_email = "test@example.com"
#         self.invalid_email = "invalid email"
        
#         # Create a test contact submission
#         ContactFormSubmission.objects.create(
#             first_name="John",
#             last_name="Doe",
#             email=self.valid_email,
#             mobile="1234567890",
#             message="Hello!"
#         )

#     def test_home_view(self):
#         response = self.client.get(reverse('home'))
#         self.assertEqual(response.status_code, 200)

#     def test_international_view(self):
#         response = self.client.get(reverse('international'))
#         self.assertEqual(response.status_code, 200)

#     def test_domestic_view(self):
#         response = self.client.get(reverse('domestic'))
#         self.assertEqual(response.status_code, 200)

#     def test_latest_updates_view(self):
#         response = self.client.get(reverse('latest_updates'))
#         self.assertEqual(response.status_code, 200)

#     def test_contact_us_post_valid(self):
#         response = self.client.post(reverse('contact_us'), {
#             'first_name': 'Alice',
#             'last_name': 'Brown',
#             'email': 'alice@example.com',
#             'mobile': '9876543210',
#             'message': 'Hello, this is a test message.'
#         })
#         self.assertRedirects(response, reverse('thank_you'))
#         self.assertTrue(ContactFormSubmission.objects.filter(email='alice@example.com').exists())

#     def test_contact_us_post_duplicate_email(self):
#         response = self.client.post(reverse('contact_us'), {
#             'first_name': 'Duplicate',
#             'last_name': 'User',
#             'email': self.valid_email,
#             'mobile': '1111111111',
#             'message': 'Duplicate test message.'
#         })
#         self.assertRedirects(response, reverse('contact_us'))
#         messages = list(response.wsgi_request._messages)
#         self.assertEqual(str(messages[0]), "This email is already registered. Please use a different one.")

#     def test_about_us_post_valid_email(self):
#         response = self.client.post(reverse('about_us'), {'email': 'newemail@example.com'})
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue(EmailSubmission.objects.filter(email='newemail@example.com').exists())

#     def test_about_us_post_duplicate_email(self):
#         EmailSubmission.objects.create(email=self.valid_email)
#         response = self.client.post(reverse('about_us'), {'email': self.valid_email})
#         self.assertEqual(response.status_code, 400)
#         self.assertTrue(EmailSubmission.objects.filter(email=self.valid_email).exists())

#     def test_about_us_post_empty_email(self):
#         response = self.client.post(reverse('about_us'), {'email': ''})
#         self.assertEqual(response.status_code, 400)

#     def test_gallery_view(self):
#         response = self.client.get(reverse('gallery'))
#         self.assertEqual(response.status_code, 200)

#     def test_gallery_videos_view(self):
#         response = self.client.get(reverse('gallery_videos'))
#         self.assertEqual(response.status_code, 200)

    
