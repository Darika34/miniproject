from rest_framework import serializers
from .models import Category, Todo

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all___'

class TodoSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Todo
        fields = '__all__'