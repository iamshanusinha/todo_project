from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializers
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class TaskPagination(PageNumberPagination):
    page_size = 5

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializers
    pagination_class = TaskPagination

class TaskDetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

    