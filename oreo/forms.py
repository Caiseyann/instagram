from django import forms
from .models import *


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['poster', 'imagecommented']

class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user_profile', 'profile','likes', 'opinions']

