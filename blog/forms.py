from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import BlogPost, UserProfile

class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "thumnail", "description", "categories" ]

class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = [ 'email','first_name', 'last_name']
        
class ProfileEditForm(ModelForm):
    class Mata:
        model = UserProfile
        excludes = ['user']
