from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'users.views',
    url(r'^new$', 'new', name='new'),
)
