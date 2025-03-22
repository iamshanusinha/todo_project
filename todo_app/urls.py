from django.urls import path 
from .views import TaskListCreateView,TaskDetailview

urlpatterns = [
    path('tasks/',TaskListCreateView.as_view(),name='task-list-creation'),
    path('tasks/<int:pk>/',TaskDetailview.as_view(),name='task-detail')
]