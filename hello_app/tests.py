from django.test import TestCase

# Create your tests here.

class HelloPageTests(SimpleTestCase):
  def test_homepage_shows_greeting(self):
    response = self.client.get('/')
    self.assertContains(response, 'Hello from Rakelle on Google CLoud!')
