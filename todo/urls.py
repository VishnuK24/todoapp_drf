from django.urls import include, path
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register('task', views.TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
