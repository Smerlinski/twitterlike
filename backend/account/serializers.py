from account.models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'id']
        extra_kwargs = {
            'username': {'validators': []},
        }
