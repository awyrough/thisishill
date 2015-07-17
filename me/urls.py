from django.conf.urls import patterns, url

urlpatterns = patterns("me.views",

                       url(r"^d3r3sum3/$", "d3_resume", name="d3_resume"),

                       url(r"^$", "me", name="me_main"),

                       )
