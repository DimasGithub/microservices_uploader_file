import os
import time

from uploaderfile.models.uploader import UploadFile
from uploaderfile.utils.validator import check_required_fields
from api.serializer.upload import UploadSerializer
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

class UploadFileViews(viewsets.GenericViewSet):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (IsAuthenticated,)
    serializer_class = (UploadSerializer)

    def upload(self, request):
        try:
            required_fields=[{'field':'file','type':InMemoryUploadedFile}]
            error_fields=check_required_fields(required_fields, request.data)
            if len(error_fields) > 0:
                response = {'status': 400}
                response.update(**error_fields)
                return Response(response, status=response.get('status'))
            file = request.FILES['file']
            fs = FileSystemStorage(base_url=os.path.join(settings.IMAGE_UPLOAD_URL, '%s' % time.strftime('%Y/%m/%d/')), location=os.path.join(settings.IMAGE_UPLOAD, '%s' % time.strftime('%Y/%m/%d/')))
            file_save = fs.save(file.name, file)
            file_url = fs.url(file_save)
            obj = UploadFile.objects.create(title=file.name, file_upload=file_save, file_path=file_url)
            obj.save()
            serializer = self.get_serializer(obj)
            result = serializer.data.get('file_path')
            response_data = {'action': True, 'message':'Success', 'results': result, 'status':status.HTTP_201_CREATED}
        except Exception as err:
            response_data = {'action': False, 'error':'process failed','status':status.HTTP_400_BAD_REQUEST}
        
        return Response(data=response_data, status=response_data.get('status'))
