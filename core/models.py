from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('done', 'Done')],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
