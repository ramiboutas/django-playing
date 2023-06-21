import json
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.core.files.base import File
from django.core.files.storage import default_storage

from .models import FolderContent


def upload_folder(request):
    obj = FolderContent.objects.create()
    directories = json.loads(request.POST["directories"])
    for (filename, path), file in zip(directories.items(), request.FILES["file_field"]):
        # default_storage.save(f"{obj.id}/{path}", ContentFile(file))
        FileSystemStorage(location=f"{settings.MEDIA_ROOT}/{obj.id}").save(path, ContentFile(file))
    return render(request, 'upload_folder.html')