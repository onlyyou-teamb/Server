from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class PostCreateForm(UserCreationForm) :
    before_image = forms.FileField()

    class Meta:
        model = User
        fields = ['title', 'content', 'before_image']

class PostUpdateForm(forms.ModelForm) :
    before_image = forms.FileField()

    class Meta:
        model = User
        fields = ['title', 'content', 'before_image']
