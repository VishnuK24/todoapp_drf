from django.db.models import Q
from rest_framework import generics, mixins, viewsets
from rest_framework import permissions
from .models import Task
from .serializers import TaskSerializer, TaskListSerializer


class TaskListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    API endpoint that allows users to be Create, list operation.
    """

    serializer_class = TaskListSerializer

    def get_queryset(self):
        """Queryset filter."""
        queryset = Task.objects.filter(is_completed=False)
        query = self.request.GET.get("q")
        if query is not None:
            queryset = Task.objects.filter(
                Q(title__icontains=query)| 
                Q(descreption__icontains=query)
                ).distinct()
        if self.request.query_params.get('expanded', '') == 'true':
            queryset = Task.objects.all().order_by('-created_on')
            return queryset
        return queryset

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be RUD operation.
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
