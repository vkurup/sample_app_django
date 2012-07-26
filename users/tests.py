import hashlib
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from models import User

class UserSignupPageTest(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('signup'))

    def test_should_have_right_content(self):
        self.assertContains(self.response, 'Sign up')

    def test_should_have_right_title(self):
        self.assertContains(self.response, '<title>Tutorial Sample App | Sign up</title>')

    def test_should_not_create_user_with_invalid_data(self):
        before_count = len(User.objects.all())
        self.client.post(reverse('new_user'), {})
        after_count = len(User.objects.all())
        self.assertEquals(before_count, after_count)

    def test_user_invalid_when_password_too_short(self):
        response = self.client.post(reverse('new_user'), {'name': 'Example User',
                                                          'email': 'user@example.com',
                                                          'password': 'a' * 5,
                                                          'password_confirmation': 'a' * 5})
        self.assertContains(response, 'Ensure this value has at least 6 characters')

    def test_user_invalid_when_password_mismatch(self):
        response = self.client.post(reverse('new_user'), {'name': 'Example User',
                                                          'email': 'user@example.com',
                                                          'password': 'foobar',
                                                          'password_confirmation': 'invalid'})
        self.assertContains(response, 'Password did not match confirmation')

    def test_should_create_user_with_valid_data(self):
        before_count = len(User.objects.all())
        self.client.post(reverse('new_user'), {'name': 'Example User',
                                               'email': 'user@example.com',
                                               'password': 'foobar',
                                               'password_confirmation': 'foobar'})
        after_count = len(User.objects.all())
        self.assertEquals(before_count + 1, after_count)


class UserProfilePageTest(TestCase):
    fixtures = ['users.json']
    def setUp(self):
        user_id = 1
        self.user = User.objects.get(id=user_id)
        self.response = self.client.get(reverse('user', args=[user_id]))

    def test_should_have_right_content(self):
        self.assertContains(self.response, self.user.name)

    def test_should_have_right_title(self):
        title = '<title>Tutorial Sample App | ' + self.user.name + '</title>'
        self.assertContains(self.response, title)

class UserTest(TestCase):
    def setUp(self):
        self.password = 'foobar'
        password_digest = hashlib.sha256(self.password).hexdigest()
        self.user = User(name='Example User',
                         email='user@example.com',
                         password_digest=password_digest)
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

    def test_authenticate_returns_user_if_password_correct(self):
        found_user = User.objects.get(email=self.user.email)
        self.assertEquals(self.user, found_user.authenticate(self.password))

    def test_authenticate_returns_false_if_password_incorrect(self):
        found_user = User.objects.get(email=self.user.email)
        self.assertFalse(found_user.authenticate('invalid'))
