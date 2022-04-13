from django.contrib import admin
from .models import Todo, Event, Category
# Register your models here.
admin.site.register(Todo)
admin.site.register(Event)
admin.site.register(Category)