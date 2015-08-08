from django.conf.urls import patterns, url

urlpatterns = patterns("users.views",
        url(r"^sign_in/$", "sign_in"),
        url(r"^sign_out/$", "sign_out"),
)
