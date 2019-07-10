from django.db import models

# Create your models here.


class MobileData(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Price = models.CharField(max_length=200)
    SmartPhone_OS = models.CharField(max_length=200)
    Img_Path = models.CharField(max_length=300)
    ScreenResolution = models.CharField(max_length=200)
    ScreenSize = models.CharField(max_length=100)
    Processor = models.CharField(max_length=100)
    GPU = models.CharField(max_length=100)
    RAM = models.CharField(max_length=100)

    def __str__(self):
        return self.Name
