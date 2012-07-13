from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

class HomePageTest(TestCase):
    def setUp(self):
        c = Client()
        self.response = c.get(reverse('home'))

    def test_should_have_right_content(self):
        """
        Home page should have the content 'Sample App'.
        """
        self.assertContains(self.response, 'Sample App')

    def test_should_have_right_title(self):
        self.assertContains(self.response, '<title>Tutorial Sample App | Home</title>')

class HelpPageTest(TestCase):
    def setUp(self):
        c = Client()
        self.response = c.get(reverse('help'))

    def test_should_have_right_content(self):
        """
        Help page should have the content 'Help'.
        """
        self.assertContains(self.response, 'Help')

    def test_should_have_right_title(self):
        self.assertContains(self.response, '<title>Tutorial Sample App | Help</title>')

class AboutPageTest(TestCase):
    def setUp(self):
        c = Client()
        self.response = c.get(reverse('about'))

    def test_should_have_right_content(self):
        """
        About page should have the content 'About Us'.
        """
        self.assertContains(self.response, 'About Us')

    def test_should_have_right_title(self):
        self.assertContains(self.response, '<title>Tutorial Sample App | About</title>')

class ContactPageTest(TestCase):
    def setUp(self):
        c = Client()
        self.response = c.get(reverse('contact'))

    def test_should_have_right_content(self):
        """
        Contact page should have the content 'Contact Me'.
        """
        self.assertContains(self.response, 'Contact Me')

    def test_should_have_right_title(self):
        self.assertContains(self.response, '<title>Tutorial Sample App | Contact Me</title>')

