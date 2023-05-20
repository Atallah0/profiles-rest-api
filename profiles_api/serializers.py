from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializer for testing our api view"""
    name = serializers.CharField(max_length=10)