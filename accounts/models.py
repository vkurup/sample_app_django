import hashlib
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import html
from microposts.models import Micropost

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    followers = models.ManyToManyField(User,
                                       related_name='follower',
                                       symmetrical=False,
                                       blank=True,
                                       null=True)
    followed_users = models.ManyToManyField(User,
                                            related_name='followed_user',
                                            symmetrical=False,
                                            blank=True,
                                            null=True)
    def __unicode__(self):
        return "%s (%s)" % (self.user.get_full_name(), self.user.email)

    def gravatar(self, size=50):
        gravatar_id = hashlib.md5(self.user.email.lower()).hexdigest()
        gravatar_url = "https://secure.gravatar.com/avatar/%s?s=%d" % (gravatar_id, size)
        name = html.escape(self.user.get_full_name())
        return '<img src="%s" alt="%s" class="gravatar" />' % (gravatar_url, name)

    def gravatar_small(self):
        return self.gravatar(30)

    def feed(self):
        user_list = [self.user]
        user_list.extend(self.followed_users.all())
        return Micropost.objects.filter(user__in=user_list)

    def following_p(self, other_user):
        return other_user in self.followed_users.all()

    def follow(self, other_user):
        self.followed_users.add(other_user)
        other_profile = other_user.get_profile()
        other_profile.followers.add(self.user)

    def unfollow(self, other_user):
        self.followed_users.remove(other_user)
        other_profile = other_user.get_profile()
        other_profile.followers.remove(self.user)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
