from rest_framework import viewsets
from rest_framework import permissions
from .models import Task
from .serializers import TaskSerializer, TaskListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be CRUD operation.
    """

    serializer_class = TaskSerializer

    def get_queryset(self):
        """Queryset filter."""
        queryset = Task.objects.all()
        if self.request.query_params.get('expanded', '') == 'true':
            queryset = Task.objects.all().order_by('-created_on')
            return queryset
        return queryset
