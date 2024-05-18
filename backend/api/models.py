from django.db import models

# Create your models here.
class Folders(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.CharField(max_length=256)
    updated_at = models.CharField(max_length=256)

class Places(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=256)
    image_url = models.CharField(max_length=256)    # image_url = models.URLField(max_length=1024, blank = True)
    memo = models.CharField(max_length=256)   # memo = models.TextField(blank=True)
    created_at = models.CharField(max_length=256)    # create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.CharField(max_length=256)   # updated_at = models.DateTimeField(auto_now=Ture)
    folder_id = models.ForeignKey('Folders', on_delete=models.CASCADE, default='')
