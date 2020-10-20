from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt

# Create your models here.
class Profile(models.Model):
    bio = HTMLFields()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    avatar = models.ImageField(upload_to='images/', blank=True)

    