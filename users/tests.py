from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

class UserPagesTest(TestCase):
    def setUp(self):
        c = Client()
        self.response = c.get(reverse('signup'))

    def test_should_have_right_content(self):
        self.assertContains(self.response, 'Sign up')

    def test_should_have_right_title(self):
        self.assertContains(self.response, '<title>Tutorial Sample App | Sign up</title>')

