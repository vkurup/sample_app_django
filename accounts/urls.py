from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'accounts.views',
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^signup/$', 'signup', name='signup'),
    url(r'^(?P<user_id>\d+)/edit$', 'edit', name='edit_user'),
    url(r'^(?P<user_id>\d+)/follow$', 'follow', name='follow_user'),
    url(r'^(?P<user_id>\d+)/unfollow$', 'unfollow', name='unfollow_user'),
    url(r'^(?P<user_id>\d+)/following$', 'following', name='following_user'),
    url(r'^(?P<user_id>\d+)/followers$', 'followers', name='followers_user'),
)

urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
)
