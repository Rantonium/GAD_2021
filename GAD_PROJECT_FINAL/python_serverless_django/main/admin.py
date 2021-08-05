from django.contrib import admin
from .models import FileList
from .models import File

admin.site.register(File)
admin.site.register(FileList)
