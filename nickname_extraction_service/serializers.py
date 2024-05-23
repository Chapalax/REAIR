from rest_framework import serializers


class TextSerializer(serializers.Serializer):
    text = serializers.EmailField(required=True)


class ValidationErrorSerializer(serializers.Serializer):
    errors = serializers.DictField(
        child=serializers.ListField(child=serializers.CharField())
    )


class PaginationSerializer(serializers.Serializer):
    page = serializers.IntegerField(min_value=1, required=True)
