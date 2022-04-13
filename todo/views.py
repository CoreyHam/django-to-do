from rest_framework import viewsets, permissions
from .models import Todo, Event, Category
from django.contrib.auth.models import User
from .serializers import *
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().select_related('created_by')
    serializer_class = TodoSerializer
    # permission_classes = [permissions.IsAuthenticated]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    