from django.db import models

# Create your models here.
class Folders(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    @staticmethod
    def get_all():
        return Folders.objects.all()
    
    @staticmethod
    def get_by_name(name):
        return Folders.objects.filter(name=name)
    
    @staticmethod
    def get_by_created_at(created_at):
        return Folders.objects.filter(created_at=created_at)

class Places(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=256)
    image_url = models.CharField(max_length=256)
    memo = models.CharField(max_length=256)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    folder_id = models.ForeignKey('Folders', on_delete=models.CASCADE, default='')
    
    @staticmethod
    def get_all():
        return Places.objects.all()
    
    @staticmethod
    def get_by_name(name):
        return Places.objects.filter(name=name)
    
    @staticmethod
    def get_by_created_at(created_at):
        return Places.objects.filter(created_at=created_at)
