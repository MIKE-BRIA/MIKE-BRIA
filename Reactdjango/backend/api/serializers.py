from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

#User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
        extra_kwargs = {'password':{'write_only': True}}
        
    def create(self,validated_data):
        print("Validated Data:", validated_data)
        user =  User.objects.create_user(**validated_data)
        return user
    
#Note serializer
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id','title','content','created_at','author']
        extra_kwargs = {'author':{'read_only': True}}