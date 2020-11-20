from django.db.models import Q
from django.views.generic import TemplateView

from rest_framework import generics, mixins, viewsets
from rest_framework import permissions

from .models import Task
from .serializers import TaskSerializer, TaskListSerializer


class TaskListAPIView(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be Create, list operation.
    """

    serializer_class = TaskListSerializer

    def get_queryset(self):
        """Queryset filter."""
        queryset = Task.objects.filter(is_completed=False)
        query = self.request.GET.get("search")
        if query is not None:
            queryset = Task.objects.filter(
                Q(title__icontains=query)| 
                Q(description__icontains=query)
                ).distinct()
        if self.request.query_params.get('expanded', '') == 'true':
            queryset = Task.objects.all().order_by('-created_on')
            return queryset
        return queryset

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class TaskRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be RUD operation.
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class TodoView(TemplateView):
    """TemplateView for display all Tasks."""

    template_name = "todo-list.html"
