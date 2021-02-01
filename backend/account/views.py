from django.shortcuts import render
from rest_framework import viewsets
from account.models import CustomUser
from account.serializers import CustomUserSerializer

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
