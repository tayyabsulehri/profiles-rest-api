from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serializer a name field for testing api view"""
    name = serializers.CharField(max_length=10)
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


