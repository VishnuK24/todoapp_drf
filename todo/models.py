from django.db import models


class Task(models.Model):
    """Task model for adding reterving tasks."""

    title = models.CharField(max_length=200)
    descreption = models.CharField(blank=True, default='', max_length=1024)
    is_completed = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['is_completed', 'created_on']
