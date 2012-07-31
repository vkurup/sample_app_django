from django.conf.urls import patterns, url

urlpatterns = patterns(
    'static_pages.views',
    url(r'^help$', 'help', name='help'),
    url(r'^about$', 'about', name='about'),
    url(r'^contact$', 'contact', name='contact'),
    )
