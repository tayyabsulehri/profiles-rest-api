from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """serializer a name field for testing api view"""
    name = serializers.CharField(max_length=10)
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UserProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model=models.UserProfile
            fields=('id','email','name','password')
            extra_kwards={
                'password':{'write_only':True,
                'style':{'input-type':'password'}
                          }
            }

        def create(self,validated_data):
            """create and return a new user"""
            user=models.UserProfile.objects.create_user(
                email=validated_data['email'],
                name = validated_data['name'],
                password=validated_data['password']

            )
            return user



