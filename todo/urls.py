from django.urls import include, path
from rest_framework import routers
from todo import views


urlpatterns = [
    path('', views.TaskListAPIView.as_view(), name='task-listcreate'),
    path('<int:pk>/', views.TaskRUDAPIView.as_view(), name='task-RUD'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
