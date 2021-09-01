from django.db import models

# Create your models here.
class photo(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    img=models.ImageField(upload_to='images')