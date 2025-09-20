from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegisetrSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only =True)

    class Meta :
        model =User
        fields = ['username','password','email']

    def create(self,validate_data):
        user =User.objects.create_user(

            username=validate_data['username'],
            email = validate_data('email'),
            password = validate_data['password']

        )
        return user
    

    
