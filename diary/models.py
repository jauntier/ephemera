

# Create your models here.
# from django.contrib.auth.models import User
# from django.db import models
# from channels.db import database_sync_to_async 
# from cloudinary.models import CloudinaryField
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync
# from rest_framework.authtoken.models import Token
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.conf import settings


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     avatar = models.ImageField(upload_to='avatars/', blank=True)

#     def __str__(self):
#         return self.user.username

# class Entry(models.Model):
#     privacy = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')], default='private')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField(blank=True)
#     photo = CloudinaryField('image', blank=True)
#     video = CloudinaryField('video', blank=True)
#     audio = CloudinaryField('audio', blank=True)
#     mood = models.CharField(max_length=20, blank=True)
#     location = models.CharField(max_length=100, blank=True)
#     activity = models.CharField(max_length=50, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
    

# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)

# def send_notification(user, text):
#     Notification.objects.create(user=user, text=text)
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.group_send)(
#         f'user_{user.id}', {'type': 'notify', 'message': text}
#     )

# @database_sync_to_async
# def get_notifications(user):
#     return Notification.objects.filter(user=user).order_by('-created_at')


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)

# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


# class Student(models.Model):
#     firstname = models.CharField(max_length=100)
#     secondname = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     age = models.IntegerField()

#     def __str__(self):
#         return f"{self.firstname} {self.secondname}"

from django.contrib.auth.models import User
from django.db import models
from channels.db import database_sync_to_async
from cloudinary.models import CloudinaryField
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.files.storage import FileSystemStorage


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
    
#     friends = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='friend_profiles')

#     def __str__(self):
#         return self.user.username

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pic/', blank=True, null=True)
    bio = models.TextField(max_length=160, blank=True, null=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.username

    def serialize(self):
        return {
            'id': self.id,
            "username": self.username,
            "profile_pic": self.profile_pic.url if self.profile_pic else None,
            "first_name": self.first_name,
            "last_name": self.last_name
        }

# Entry model
class Entry(models.Model):
    privacy = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')], default='private')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    photo = CloudinaryField('image', blank=True, resource_type='image')
    video = CloudinaryField('video', blank=True, resource_type='video')
    audio = CloudinaryField('audio', blank=True, resource_type='video')
    mood = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    activity = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Notification model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

# Function to send notifications
def send_notification(user, text):
    Notification.objects.create(user=user, text=text)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'user_{user.id}', {'type': 'notify', 'message': text}
    )

@database_sync_to_async
def get_notifications(user):
    return Notification.objects.filter(user=user).order_by('-created_at')

# FriendRequest model
class FriendRequest(models.Model):
   
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests',)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='pending')

    def accept(self):
        self.status = 'accepted'
        self.save()
        self.from_user.friends.add(self.to_user)
        self.to_user.friends.add(self.from_user)

    def decline(self):
        self.status = 'declined'
        self.save()

class Post(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    date_created = models.DateTimeField(default=timezone.now)
    content_text = models.TextField(max_length=140, blank=True)
    content_image = models.ImageField(upload_to='posts/', blank=True, null=True) 
    likers = models.ManyToManyField(User, blank=True , related_name='likes')
    savers = models.ManyToManyField(User,blank=True , related_name='saved')
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Post ID: {self.id} (creater: {self.creater})"

    def img_url(self):
        return self.content_image.url

    def append(self, name, value):
        self.name = value

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenters')
    comment_content = models.TextField(max_length=90)
    comment_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Post: {self.post} | Commenter: {self.commenter}"

    def serialize(self):
        return {
            "id": self.id,
            "commenter": self.commenter.serialize(),
            "body": self.comment_content,
            "timestamp": self.comment_time.strftime("%b %d %Y, %I:%M %p")
        }
    
class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    followers = models.ManyToManyField(User, blank=True, related_name='following')

    def __str__(self):
        return f"User: {self.user}"
        
# class Student(models.Model):
#     firstname = models.CharField(max_length=100)
#     secondname = models.CharField(max_length = 100)
#     email = models.EmailField(unique = True)
#     age = models.IntegerField()

#     def __str__(self):
#         return f"{self.firstname} {self.secondname}"
    