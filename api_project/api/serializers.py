from rest_framework import serializers
from .models import Book
from datetime import datetime
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']
        read_only_fields = ['id']  # id field is read-only and auto-generated
        days_since_model_creation = serializers.SerializerMethodField()
        created_at = serializers.DateTimeField(read_only=True)
    # Custom field to calculate days since model creation
    # This assumes the model has a created_at field, which is not defined in the current
    def get_days_since_model_creation(self, obj):
        return (datetime.now() - obj.created_at)
    