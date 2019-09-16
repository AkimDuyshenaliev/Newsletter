from django.db import models

# Create your models here.
class SaveTextFileModel(models.Model):
    fileTXT = models.FileField(verbose_name='Upload .txt with emails (not working yet)')


