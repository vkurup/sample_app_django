from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from models import User

class UserPagesTest(TestCase):
    def setUp(self):
        c = Client()
        self.response = c.get(reverse('signup'))

    def test_should_have_right_content(self):
        self.assertContains(self.response, 'Sign up')

    def test_should_have_right_title(self):
        self.assertContains(self.response, '<title>Tutorial Sample App | Sign up</title>')

class UserTest(TestCase):
    def setUp(self):
        self.user = User(name='Example User', email='user@example.com')
        self.user.save()

    def test_name_present(self):
        self.assertIsNotNone(self.user.name)

    def test_email_present(self):
        self.assertIsNotNone(self.user.email)

    def test_password_present(self):
        self.assertIsNotNone(self.user.password_digest)

    def test_user_valid(self):
        self.user.full_clean()
        self.assertTrue(self.user)

    def test_user_invalid_when_name_absent(self):
        self.user.name = ''
        self.assertRaisesMessage(ValidationError, '', self.user.full_clean)

    def test_user_invalid_when_email_absent(self):
        self.user.email = ''
        self.assertRaisesMessage(ValidationError, '', self.user.full_clean)

    def test_user_invald_when_name_too_long(self):
        self.user.name = 'a' * 51
        self.assertRaisesMessage(ValidationError, '', self.user.full_clean)
        
    def test_user_invalid_when_email_invalid(self):
        addresses = 'user@foo,com user_at_foo.org example.user@foo. foo@bar_baz.com foo@bar+baz.com'.split()
        for email in addresses:
            self.user.email = email
            self.assertRaisesMessage(ValidationError, 'Enter a valid e-mail address', self.user.full_clean)
        
    def test_user_valid_when_email_valid(self):
        addresses = 'user@foo.COM A_US-ER@f.b.org frst.lst@foo.jp a+b@baz.cn'.split()
        for email in addresses:
            self.user.email = email
            self.user.full_clean()
            self.assertTrue(self.user)

    def test_user_invalid_when_email_taken(self):
        self.user.id = None
        user_with_same_email = self.user
        user_with_same_email.email = self.user.email.upper()
        self.assertRaisesMessage(ValidationError, '', user_with_same_email.full_clean)
