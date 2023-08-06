from django.db.migrations import serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from rest_framework import viewsets, status
from rest_framework import permissions
from .serializers import CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})