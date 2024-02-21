from rest_framework import serializers
from app.models import Category
from rest_framework.validators import UniqueValidator
from app.category.accessor import CategoryAccessor


# https://www.django-rest-framework.org/api-guide/serializers/#validation
# https://stackoverflow.com/a/27591842
# https://stackoverflow.com/a/31278625
class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=255,
        validators=[UniqueValidator(queryset=CategoryAccessor.get_all_categories())],
    )

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']

    def validate_name(self, value):
        value = value.capitalize()
        valid_names = [choice[0] for choice in Category.CATEGORY_CHOICES]
        if value not in valid_names:
            raise serializers.ValidationError("Invalid category name.")
        return value

    def update(self, instance, validated_data):
        if 'name' in validated_data:
            del validated_data['name']
        return super().update(instance, validated_data)
