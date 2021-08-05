from django.db import models


class FileList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class File(models.Model):
    file_user_id = models.IntegerField(default=0)
    file_name = models.CharField(max_length=100)
    file_extension = models.CharField(max_length=10)
    file_type = models.CharField(max_length=255)

    @classmethod
    def create(cls, file_user_id, file_name, file_extension, file_type):
        file = cls(file_user_id=file_user_id, file_name=file_name, file_extension=file_extension,
                   file_type=file_type)
        return file

    def _str__(self):
        return self.file_type + " " + self.file_name + " " + self.file_extension
