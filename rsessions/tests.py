from django.test import TestCase
from django.core.urlresolvers import reverse

class AuthenticationTest(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('signin'))

    def test_should_have_right_content(self):
        self.assertContains(self.response, 'Sign in')

    def test_should_have_right_title(self):
        self.assertContains(self.response, '<title>Tutorial Sample App | Sign in</title>')

    def test_login_fails_when_input_blank(self):
        response = self.client.post(reverse('signin'), {'email': '',
                                                        'password': '',})
        self.assertContains(response, 'This field is required')

    def test_login_fails_when_password_wrong(self):
        response = self.client.post(reverse('signin'), 
                                    data={'email': 'joe@example.com',
                                          'password': 'invalid',},
                                    follow=True)
        self.assertContains(response, 'Invalid email/password combination.')

