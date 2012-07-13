from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^signup', 'users.views.new', name='signup'),
    url(r'^users/', include('users.urls')),
    url(r'', include('static_pages.urls')),
    # Examples:
    # url(r'^$', 'sample_app.views.home', name='home'),
    # url(r'^sample_app/', include('sample_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
