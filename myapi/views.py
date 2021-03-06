from django.shortcuts import render
from .serializers import HeroSerializer
from .models import Hero
from rest_framework import viewsets

# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer