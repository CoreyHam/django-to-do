from django.urls import path, include
from rest_framework import routers
from .views import TodoViewSet, EventViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('todo', TodoViewSet)
router.register('event', EventViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]