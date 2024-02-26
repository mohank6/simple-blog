from rest_framework import serializers


class RefreshTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()

    def to_representation(self, instance):
        return {
            'access_token': str(instance.access_token),
            'refresh_token': str(instance),
        }
