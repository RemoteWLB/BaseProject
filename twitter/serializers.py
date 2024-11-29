from rest_framework import serializers
from twitter.models import MappTree, Twitter
from utils.fields import ReadWriteSerializerMethodField

class MappTreeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MappTree
        fields = "__all__"
        

class TwitterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Twitter
        fields = "__all__"