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
    followers = models.ManyToManyField('self',
                                       related_name='follower',
                                       symmetrical=False,
                                       blank=True,
                                       null=True)
    followed_users = models.ManyToManyField('self',
                                            related_name='followed_user',
                                            symmetrical=False,
                                            blank=True,
                                            null=True)

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
        user_list = [self]
        user_list.extend(self.followed_users.all())
        return Micropost.objects.filter(user__in=user_list)

    def following_p(self, other_user):
        return other_user in self.followed_users.all()

    def follow(self, other_user):
        self.followed_users.add(other_user)
        other_user.followers.add(self)

    def unfollow(self, other_user):
        self.followed_users.remove(other_user)
        other_user.followers.remove(self)

    def gravatar(self, size=50):
        gravatar_id = hashlib.md5(self.email.lower()).hexdigest()
        gravatar_url = "https://secure.gravatar.com/avatar/%s?s=%d" % (gravatar_id, size)
        name = html.escape(self.name)
        return '<img src="%s" alt="%s" class="gravatar" />' % (gravatar_url, name)

    def gravatar_small(self):
        return self.gravatar(30)
