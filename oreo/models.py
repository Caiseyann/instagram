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
    def get_all_profiles(cls): 
        profile = Profile.objects.get(user = id)
        return profile 
    
    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    @classmethod
    def get_profile(cls, id):
        profile = Profile.objects.all()
        return profile 

    @classmethod
    def find_profile(cls, search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile

    class Meta:
        ordering = ['user']

class Likes(models.Model):
	post = models.IntegerField()
	liker = models.CharField(max_length=20)


class Comment(models.Model):
    comment = models.CharField(max_length=30, blank=True)
    poster = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    imagecommented = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments',null=True)

    def save_comment(self):
        self.save()

    @classmethod
    def get_all_comments(cls):
        comments = Comment.objects.all()
        return comments

    @classmethod
    def get_comments(cls, id):
        comments = Comment.objects.filter(post_id=id).all()
        return comments

    def __str__(self):
        return self.comment
