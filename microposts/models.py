from django.db import models

class Micropost(models.Model):
    content = models.TextField(max_length=140)
    user = models.ForeignKey('users.User', editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s: %s" % (self.user, self.content)

    class Meta:
        ordering = ['-created_at']
