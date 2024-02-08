from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# uzyj python manage.py shell by moc sobie importowac modelsony tak o
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    completed = models.BooleanField()
    creation_date = models.DateTimeField(default=timezone.now, editable=False)
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"({self.todolist=}, {self.text}, {self.completed}, {self.creation_date}, {self.end_date})"