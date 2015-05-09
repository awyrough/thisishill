from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'thisishill.views.landing', name='landing'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^me/', include('me.urls')),
)
