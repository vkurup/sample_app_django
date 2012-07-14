import hashlib
from django.core.exceptions import ValidationError
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password_digest = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    password = ''
    password_confirmation = ''

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.email)

    def clean(self):
        self.email = self.email.lower()

        if self.password.strip() == '':
            raise ValidationError('Password cannot be blank')
        if len(self.password.strip()) < 6:
            raise ValidationError('Password too short')
        if self.password == self.password_confirmation:
            self.password_digest = hashlib.sha256(self.password).hexdigest()
        else:
            raise ValidationError('Password must match confirmation')

    def save(self, *args, **kwargs):
        self.full_clean()
        super(User, self).save(*args, **kwargs)

    def authenticate(self, password):
        digest = hashlib.sha256(password).hexdigest()
        if digest == self.password_digest:
            return self
        else:
            return False

