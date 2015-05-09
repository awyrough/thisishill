from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import settings

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'thisishill.views.landing', name='landing'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^me/', include('me.urls')),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.STATIC_ROOT}))