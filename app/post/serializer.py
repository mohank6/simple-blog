from rest_framework import serializers
from django.utils.text import slugify
from app.models import Post


class PostSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'categories',
            'author',
            'content',
            'created_at',
            'updated_at',
            'is_published',
        ]

    def create(self, validated_data):
        title = validated_data.get('title')
        slug = slugify(title)
        validated_data['slug'] = slug
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'author' in validated_data:
            del validated_data['author']
        if 'title' in validated_data:
            validated_data['slug'] = slugify(validated_data.get('title'))
        return super().update(instance, validated_data)

    def validate(self, attrs):
        if 'author' in attrs and not attrs.get('author').is_active:
            raise serializers.ValidationError("Author doesnot exists.")
        return attrs
