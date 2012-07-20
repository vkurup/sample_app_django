from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'rsessions.views',
    url(r'^new$', 'new', name='new_session'),
    url(r'^delete$', 'delete', name='delete_session'),
)
