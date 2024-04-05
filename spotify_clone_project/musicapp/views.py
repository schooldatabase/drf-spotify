
from rest_framework import generics, permissions, status, filters
from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import *
from .serializers import *
# from .models import Artist, Song, Podcast, Playlist, Album, Blend, PremiumPlan
# from .serializers import ArtistSerializer, SongSerializer, PodcastSerializer, PlaylistSerializer, AlbumSerializer, BlendSerializer, PremiumPlanSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

class ArtistListView(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # permission_classes = [permissions.IsAuthenticated]

class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['artist__name']
    search_fields = ['title', 'artist__name']
    # permission_classes = [permissions.IsAuthenticated]

# Add similar views for Podcast, Playlist, Album, Blend, PremiumPlan
class PlaylistCreateView(generics.CreateAPIView):
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

class PlaylistAddRemoveSongView(generics.UpdateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    # permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        playlist = self.get_object()
        song_id = self.request.data.get('song_id')
        action = self.request.data.get('action')  # 'add' or 'remove'

        if action == 'add':
            if playlist.songs.filter(id=song_id).exists():
                return Response({"detail": "Song already exists in the playlist."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                song = Song.objects.get(id=song_id)
                playlist.songs.add(song)
        elif action == 'remove':
            if playlist.songs.filter(id=song_id).exists():
                song = Song.objects.get(id=song_id)
                playlist.songs.remove(song)
            else:
                return Response({"detail": "Song does not exist in the playlist."}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

class CollaborativePlaylistView(generics.UpdateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    # permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        playlist = self.get_object()
        user_id = self.request.data.get('user_id')
        action = self.request.data.get('action')  # 'add' or 'remove'

        user = get_object_or_404(settings.AUTH_USER_MODEL, id=user_id)

        if action == 'add':
            playlist.collaborators.add(user)
        elif action == 'remove':
            playlist.collaborators.remove(user)

        serializer.save()
        

class PodcastCreateView(generics.CreateAPIView):
    serializer_class = PodcastSerializer
    # permission_classes = [IsAuthenticated]

class PodcastDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    # permission_classes = [IsAuthenticated]
    
class AlbumCreateView(generics.CreateAPIView):
    serializer_class = AlbumSerializer
    # permission_classes = [IsAuthenticated]

class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    # permission_classes = [IsAuthenticated]
    
class PremiumPlanCreateView(generics.CreateAPIView):
    serializer_class = PremiumPlanSerializer
    # permission_classes = [IsAuthenticated]

class PremiumPlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PremiumPlan.objects.all()
    serializer_class = PremiumPlanSerializer
    # permission_classes = [IsAuthenticated]