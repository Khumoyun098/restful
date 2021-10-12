from rest_framework import serializers

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from dev.models import Car


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data["username"]
        password = data["password"]
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated."
                    raise serializers.ValidationError(msg)
            else:
                msg = "Unable to login with given credentials."
                raise serializers.ValidationError(msg)
        else:
            msg = "Must provide username and password both."
            raise serializers.ValidationError(msg)
        return data

    class Meta:
        model = User
        fields = ['username', 'password']
        read_only_fields = ('password',)