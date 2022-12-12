from django.contrib import admin

# Register your models here.
from uploaderfile.models.uploader import UploadFile
# Register your models here.
admin.site.register(UploadFile)