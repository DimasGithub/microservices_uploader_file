
from rest_framework import serializers
from uploaderfile.models.uploader import UploadFile

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFile
        fields = ('title', 'file_upload', 'file_path')