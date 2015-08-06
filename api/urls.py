from django.conf.urls import url, include
from rest_framework import routers

from api import views as api_views

router = routers.DefaultRouter()

router.register(r"is_this_working", api_views.IsThisWorkingViewSet, base_name="is_this_working")

urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
