from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt

# Create your models here.
class Profile(models.Model):
    bio = HTMLFields()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    avatar = models.ImageField(upload_to='images/', blank=True)

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls): 
        profile = Profile.objects.get(user = id)
        return profile 

    @classmethod
    def get_profile(cls, id):
        profile = Profile.objects.all()
        return profile 