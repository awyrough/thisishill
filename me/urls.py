from django.conf.urls import patterns, include, url

urlpatterns = patterns("me.views",

    url(r"^", "me", name="me"),
    
)
