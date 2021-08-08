from rest_framework import serializers

from django.contrib.auth.models import User, Group
from dev.models import Car


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

