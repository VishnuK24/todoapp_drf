from django.urls import include, path
from rest_framework import routers
from todo import views

app_name = 'todo'

urlpatterns = [
    path('', views.TaskListAPIView.as_view(), name='list'),
    path('<int:pk>/', views.TaskRUDAPIView.as_view(), name='detail'),
]
