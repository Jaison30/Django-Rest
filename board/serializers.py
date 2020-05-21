from django.contrib.auth.models import User
from rest_framework import serializers

from django.contrib.auth import authenticate

from .models import Sprint, Task

from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('id','username','is_active')


class SprintSerializer(serializers.ModelSerializer):


    class Meta:
        model = Sprint
        fields = ('id','name','description','end')


class TaskSerializer(serializers.ModelSerializer):

    status_display = serializers.SerializerMethodField()

    


    class Meta:
        model = Task
        fields = ('id','name','description','sprint','status','order','assigned','started','due','completed','status_display')


    def get_status_display(self, obj):
        return obj.get_status_display()


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    default_error_messages = {
        'inactive_account': 'User account is disabled.',
        'invalid_credentials': 'Unable to login with provided credentials.'
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        self.user = authenticate(username=attrs.get("username"), password=attrs.get('password'))
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(self.error_messages['inactive_account'])
            return attrs
        else:
            raise serializers.ValidationError(self.error_messages['invalid_credentials'])


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ("auth_token", "created")


    


