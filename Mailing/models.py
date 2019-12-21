from django.db import models

# Create your models here.
class SaveTextFileModel(models.Model):
    fileTXT = models.FileField(
        verbose_name='Upload .txt with emails (not working yet)', blank=True)


class DepartmentModel(models.Model):
    name = models.CharField(max_length=80, default="")

    def __str__(self):
        return self.name


class UserModel(models.Model):
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.department

class MessageModel(models.Model):
    sendDate = models.DateField()
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    subject = models.CharField(max_length=80, default="")
    message = models.TextField(default="")

    def __str__(self):
        return("Message content")

