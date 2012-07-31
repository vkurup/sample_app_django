from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^users/(?P<username>\w+)', 'accounts.views.show', name='user'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^microposts/', include('microposts.urls')),
    url(r'^$', 'microposts.views.home', name='home'),
    url(r'', include('static_pages.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    )
