from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'author',
            'CF_username',
            'CF_rating',
            'SEM_SPI_List',
            'created_on'
        ]