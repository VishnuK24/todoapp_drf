from rest_framework import serializers

from .models import Task


class TaskListSerializer(serializers.ModelSerializer):
    """TaskListSerializer for list Task instance"""

    class Meta:
        model = Task
        fields = ['id', 'title', 'descreption', 'is_completed']


class TaskSerializer(serializers.ModelSerializer):
    """Task serializer for Task instance"""

    class Meta:
        model = Task
        fields = '__all__'
