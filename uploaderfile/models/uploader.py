from django.db import models

from uploaderfile.models.mixins import TimestampModel

class UploadFile(TimestampModel):
    title = models.CharField(max_length = 150)
    file_upload = models.FileField(upload_to=None, max_length = 100)
    file_path = models.CharField(max_length=150)
        
    class Meta:
        db_table = 'uploadfile'
        permissions= (
            ('read-upload-file', 'can read file'),
            ('delete-upload-file', 'can  delete file'),
            ('edit-upload-file', 'can edit file'),
            ('create-upload-file', 'can create file')
        )