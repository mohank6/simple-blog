from rest_framework import serializers
from app.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    is_approved = serializers.BooleanField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'name',
            'email',
            'content',
            'is_approved',
            'created_at',
        ]

    def update(self, instance, validated_data):
        validated_data.pop('post', None)
        validated_data.pop('email', None)
        return super().update(instance, validated_data)
