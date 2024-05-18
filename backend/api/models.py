from django.db import models

# Create your models here.
class Folders(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Places(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=256)
    image_url = models.CharField(max_length=256)
    memo = models.CharField(max_length=256)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    folder_id = models.ForeignKey('Folders', on_delete=models.CASCADE, default='')
