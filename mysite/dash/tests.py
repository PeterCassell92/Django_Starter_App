from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from polls.models import Question


class DashAppTest(TestCase):
    
    def setUp(self):
        # Create some test questions
        Question.objects.create(question_text="What is your favorite color?", pub_date=timezone.now())
        Question.objects.create(question_text="What is the capital of France?", pub_date=timezone.now())

    def test_dash_link_to_polls(self):
        # Get the response from the Dash index page
        response = self.client.get(reverse('dash:index'))  # Use reverse to get the URL for the Dash index view
        
        # Ensure the page loads successfully (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check if the 'Go to Polls' link is in the response HTML
        # You should check the exact anchor tag and href attribute
        self.assertContains(response, '<a href="/polls/">Go to Polls</a>')
    
    def test_polls_home_page(self):
        # Test if the /polls/ page renders correctly with questions
        response = self.client.get(reverse('polls:polls_home'))
        
        # Ensure the page loads successfully (status code 200)
        self.assertEqual(response.status_code, 200)

        # Ensure the questions are rendered on the page
        self.assertContains(response, "What is your favorite color?")
        self.assertContains(response, "What is the capital of France?")
    
    def test_no_questions(self):
        # If no questions are in the database, the page should show "No polls are available."
        
        # First, delete all questions from the database
        Question.objects.all().delete()

        # Now visit the polls home page
        response = self.client.get(reverse('polls:polls_home'))

        # Ensure the page loads successfully (status code 200)
        self.assertEqual(response.status_code, 200)

        # Ensure the "No polls are available" message is displayed
        self.assertContains(response, "No polls are available.")
