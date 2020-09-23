from rest_framework import serializers

from .models import Task


class TaskListSerializer(serializers.ModelSerializer):
    """TaskListSerializer for list Task instance"""

    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Task
        fields = ['url', 'id', 'title', 'descreption', 'is_completed']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)


class TaskSerializer(serializers.ModelSerializer):
    """Task serializer for Task instance"""

    class Meta:
        model = Task
        fields = '__all__'
