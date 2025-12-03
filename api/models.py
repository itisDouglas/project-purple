from django.db import models
from django.conf import settings

# Create your models here.

# models to create:
# Profile
# Post
# Comment

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                on_delete=models.CASCADE) 
    
    sexual_orientation = models.CharField(max_length=50, blank=True, null=True)
    aro_spec_identity = models.CharField(max_length=50, blank=True, null=True)
    ace_spec_identity = models.CharField(max_length=50, blank=True, null=True)
    pronouns = models.CharField(max_length=20, blank=True, null=True)
    relationship_style = models.CharField(max_length=50, blank=True, null=True)

    background_color = models.CharField(max_length=7, default='#FFFFFF')
    accent_color = models.CharField(max_length=7, default='#000000')
    identity_block_text = models.TextField(blank=True)

    bio = models.TextField()
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Profile for {self.user.username}"

class Post(models.Model):
    title = models.CharField(max_length=150)
    post  = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.user.username} on Post {self.post.id}"
