from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'users.views',
    url(r'^$', 'index', name='users'),
    url(r'^(?P<user_id>\d+)$', 'show', name='user'),
    url(r'^(?P<user_id>\d+)/edit$', 'edit', name='edit_user'),
    url(r'^(?P<user_id>\d+)/following$', 'following', name='following_user'),
    url(r'^(?P<user_id>\d+)/followers$', 'followers', name='followers_user'),
    url(r'^(?P<user_id>\d+)/follow$', 'follow', name='follow_user'),
    url(r'^(?P<user_id>\d+)/unfollow$', 'unfollow', name='unfollow_user'),
    url(r'^new$', 'new', name='new_user'),
)
