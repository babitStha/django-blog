from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile = models.ImageField(blank=True, null=True, default="default-thumnail.jpg")
    bio = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    contact = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return str(self.user.username)


class BlogCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class BlogPost(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    thumnail = models.ImageField(blank=True, null=True, default="default-thumnail.jpg")
    description = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(BlogCategory, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return f"{self.author.user.username} || {self.title}"




