from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Banner(models.Model):
    banner = models.ImageField(upload_to = 'bannerimg' )

