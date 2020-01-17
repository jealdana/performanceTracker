from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import MetricSerializer      
from .models import Metric                     

# Create your views here.
class MetricView(viewsets.ModelViewSet):
  serializer_class = MetricSerializer
  queryset = Metric.objects.all()
