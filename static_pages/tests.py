from django.test import TestCase
from django.test.client import Client

class HomePageTest(TestCase):
    def test_should_have_right_content(self):
        """
        Home page should have the content 'Sample App'.
        """
        c = Client()
        response = c.get('/static_pages/home')
        self.assertContains(response, 'Sample App')

    def test_should_have_right_title(self):
        c = Client()
        response = c.get('/static_pages/home')
        self.assertContains(response, '<title>Tutorial Sample App | Home</title>')

class HelpPageTest(TestCase):
    def test_should_have_right_content(self):
        """
        Help page should have the content 'Help'.
        """
        c = Client()
        response = c.get('/static_pages/help')
        self.assertContains(response, 'Help')

    def test_should_have_right_title(self):
        c = Client()
        response = c.get('/static_pages/help')
        self.assertContains(response, '<title>Tutorial Sample App | Help</title>')

class AboutPageTest(TestCase):
    def test_should_have_right_content(self):
        """
        About page should have the content 'About Us'.
        """
        c = Client()
        response = c.get('/static_pages/about')
        self.assertContains(response, 'About Us')

    def test_should_have_right_title(self):
        c = Client()
        response = c.get('/static_pages/about')
        self.assertContains(response, '<title>Tutorial Sample App | About</title>')

