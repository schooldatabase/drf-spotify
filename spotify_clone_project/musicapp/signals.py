# signals.py
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Playlist

@receiver(m2m_changed, sender=Playlist.songs.through)
def update_song_count(sender, instance, **kwargs):
    instance.song_count = instance.songs.count()
    instance.save()
