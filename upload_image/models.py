from django.db import models


class UploadedFile(models.Model):
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return self.name + ":" + self.file.name

# Create your models here.
