import hashlib
from django.db import models
from django.utils import html
from microposts.models import Micropost

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password_digest = models.CharField(max_length=200, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.email)

    def clean(self):
        self.email = self.email.lower()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(User, self).save(*args, **kwargs)

    def authenticate(self, password):
        digest = hashlib.sha256(password).hexdigest()
        if digest == self.password_digest:
            return self
        else:
            return False

    def get_absolute_url(self):
        return "/users/%i" % self.id

    def feed(self):
        return Micropost.objects.filter(user=self.id)

    def gravatar(self):
        gravatar_id = hashlib.md5(self.email.lower()).hexdigest()
        gravatar_url = "https://secure.gravatar.com/avatar/%s" % (gravatar_id)
        name = html.escape(self.name)
        return '<img src="%s" alt="%s" class="gravatar" />' % (gravatar_url, name)
