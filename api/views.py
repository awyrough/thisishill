# from thisishill.loggers import logger

# DRF packages
from rest_framework import viewsets
# from rest_framework.exceptions import ValidationError, PermissionDenied
# from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
# from rest_framework.decorators import list_route
# from rest_framework.authtoken.models import Token


class IsThisWorkingViewSet(viewsets.ViewSet):

    """
    Testing API.
    """

    def list(self, request):
        return Response({
                "result": "Hello, world!"
            })
