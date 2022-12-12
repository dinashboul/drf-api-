from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import SnackSerializer
# Create your views here.
from .models import Snacks


class SnackListView(ListCreateAPIView):
    queryset=Snacks.objects.all()
    serializer_class= SnackSerializer


class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Snacks.objects.all()
    serializer_class= SnackSerializer