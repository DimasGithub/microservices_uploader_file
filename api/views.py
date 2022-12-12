import os
import time

from uploaderfile.models.uploader import UploadFile
from api.serializer.upload import UploadSerializer
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# from django.utils.translation import ugettext_lazy as _

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
            file = request.FILES['file']
            fs = FileSystemStorage(location=os.path.join(settings.IMAGE_UPLOAD, '%s' % time.strftime('%Y/%m/%d/')))
            file_save = fs.save(file.name, file)
            file_url = fs.url(file_save)
            obj = UploadFile.objects.create(title=file.name, file_upload=file_save, file_path=file_url)
            obj.save()
            serializer = self.get_serializer(obj)
            response_data = {'action': True, 'message':'Success', 'results': serializer.data, 'status':status.HTTP_201_CREATED}
        except Exception as err:
            response_data = {'action': False, 'error':'process failed','status':status.HTTP_400_BAD_REQUEST}
        
        return Response(data=response_data, status=response_data.get('status'))
