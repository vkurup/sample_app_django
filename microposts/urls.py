from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'microposts.views',
    url(r'^new$', 'new', name='new_micropost'),
    url(r'^(?P<mp_id>\d+)/delete$', 'delete', name='delete_micropost'),
)
