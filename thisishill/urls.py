from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin

import settings

admin.autodiscover()

urlpatterns = patterns("",
                       url(r"^admin/", include(admin.site.urls)),
                       url(r"^sign_in/$", "sign_in"),
                       url(r"^sign_out/$", "sign_out"),

                       # main landing page / index
                       url(r"^$", "thisishill.views.landing", name="landing"),

                       # me app
                       url(r"^me/", include("me.urls")),

                       # define project app URLs
                       url(r"^projects/", include("trailheadlane.urls")),

                       # API
                       url(r"^api/v1/", include("api.urls")),
                       url(r"^api/", RedirectView.as_view(url="/api/v1/")),


                       )

urlpatterns += patterns("",
                        (r"^static/(?P<path>.*)$", "django.views.static.serve", {
                            "document_root": settings.STATIC_ROOT}))
