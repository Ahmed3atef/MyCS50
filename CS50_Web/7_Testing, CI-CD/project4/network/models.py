from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Tweet(models.Model):
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    content = models.TextField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name="likes")
    
    
    def serialize(self):
        return {
            "id":self.id,
            "owner":self.owner.id,
            "content":self.content,
            "timestamp":self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "likes":self.likes.count()
        }
        
    def __str__(self):
        return f"author:{self.owner} write {self.content} on {self.timestamp.strftime('%b %d %Y, %I:%M %p')} and many likes he get {self.likes.count()}"


class Follow(models.Model):
    
    following = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="following")
    followers = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="followers")
    
    def __str__(self):
        return f"You following {self.following} and people follow you {self.followers}"