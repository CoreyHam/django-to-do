from .models import Todo, Event, Category
from django.contrib.auth.models import User
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
    )
    class Meta:
        model = Todo
        fields = [
            'id',
            'title',
            'description',
            'priority',
            'completed',
            'category',
            'created_at',
            'updated_at',
            'created_by'
        ]

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'category',
            'start_date',
            'end_date',
            'created_at',
            'updated_at',
            'created_by',
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'created_at',
            'updated_at',
        ]
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user