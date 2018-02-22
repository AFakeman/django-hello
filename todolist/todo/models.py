from django.db import models
from django.contrib.auth.models import User


class ToDoItem(models.Model):
    text = models.CharField(max_length=280)
    done = models.BooleanField(default=False)
    create_date = models.DateTimeField('creation date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
