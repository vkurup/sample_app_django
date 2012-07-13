from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'static_pages.views',
    url(r'^home$', 'home'),
    url(r'^help$', 'help'),
    url(r'^about$', 'about'),
    url(r'^contact$', 'contact'),
    # Examples:
    # url(r'^$', 'sample_app.views.home', name='home'),
    # url(r'^sample_app/', include('sample_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
