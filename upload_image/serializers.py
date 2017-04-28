from rest_framework import serializers
from upload_image.models import Upload_image
import random
from random import randint
import json
import time
import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config( 
  cloud_name = "aiffin", 
  api_key = "494554345493443", 
  api_secret = "8xgayEXKg_U2aanHYHZcV_sJBhc" 
)

class Upload_imageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upload_image
        fields = ('pk','photo','name')

    def create(self, validated_data):
    
        public_id='id'+str(random.randint(100000, 999999))

        
        if(bool(validated_data.get('photo')) == True):
         cloudinary.uploader.upload(validated_data.get('photo'),public_id ="aiffin/"+public_id)

        if(bool(validated_data.get('photo')) == True):
         link=public_id+".jpg"

        objects=Upload_image.objects.create(photo=link,link=link,name=validated_data.get('photo'))

        return objects
