from django.db import models
import uuid
# from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

class BaseModel(models.Model):
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        

class Artist(BaseModel):
    name = models.CharField(max_length=100)
    performed_by = models.CharField(max_length=100)
    written_by = models.CharField(max_length=100)
    produced_by = models.CharField(max_length=100)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='following_artists')

class Song(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    audio_url = models.URLField()
    video_url = models.URLField()
    likes = models.PositiveIntegerField(default=0)
    downloads = models.PositiveIntegerField(default=0)

class Podcast(BaseModel):
    title = models.CharField(max_length=100)
    audio_url = models.URLField()
    video_url = models.URLField()
    watching_choices = models.CharField(max_length=10, choices=[('low', 'Low'), ('normal', 'Normal'), ('high', 'High')])


class Playlist(BaseModel):
    
    PUBLIC = 'public'
    PRIVATE = 'private'
    IS_PUBLIC_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    ]
    
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, related_name='playlists')
    is_public = models.CharField(max_length=10, choices=IS_PUBLIC_CHOICES)
    # is_public = models.BooleanField(default=True)
    enhanced = models.BooleanField(default=False)

class Album(BaseModel):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, related_name='albums')

class Blend(BaseModel):
    title = models.CharField(max_length=100)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

class PremiumPlan(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    months = models.PositiveIntegerField(choices=[(1, '1 Month'), (2, '2 Months'), (3, '3 Months')])
    is_active = models.BooleanField(default=True)   
# Add more fields and functionalities as needed
