from django.db import models
from accounts.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(max_length=1200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

