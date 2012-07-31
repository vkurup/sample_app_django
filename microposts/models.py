from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import html
import hashlib

class Micropost(models.Model):
    content = models.TextField(max_length=140)
    user = models.ForeignKey('users.User', editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s: %s" % (self.user, self.content)

    class Meta:
        ordering = ['-created_at']

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def gravatar(self, size=50):
        gravatar_id = hashlib.md5(self.user.email.lower()).hexdigest()
        gravatar_url = "https://secure.gravatar.com/avatar/%s?s=%d" % (gravatar_id, size)
        name = html.escape(self.user.get_full_name())
        return '<img src="%s" alt="%s" class="gravatar" />' % (gravatar_url, name)

    def feed(self):
        return None

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
