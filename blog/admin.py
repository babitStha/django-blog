from django.contrib import admin
from . models import UserProfile, BlogPost, BlogCategory

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(BlogPost)
admin.site.register(BlogCategory)
