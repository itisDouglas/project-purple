from django.db import models
from django.conf import settings

# Create your models here.

# models to create:
# User
# Profile
# Post
# Comment

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=12)
    password = models.CharField(max_length=24)
    email = models.EmailField(max_length=254)

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    bio = models.TextField()
    birthdate = models.DateField(null=True, blank=True)

class Post(models.Model):
    title = models.CharField(max_length=42)
    post  = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

