from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ManyToManyField('Category')
    priority = models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=10)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos', null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ManyToManyField('Category')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events', null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'