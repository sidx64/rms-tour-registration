from rest_framework import serializers
from registration.models import RMSIndia2019


class RMSIndia2019Serializer(serializers.ModelSerializer):
    class Meta:
        model = RMSIndia2019
        fields = '__all__'
