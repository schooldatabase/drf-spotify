from django.urls import path
from .views import (
    ArtistListView, SongListView,
    PlaylistCreateView, PlaylistDetailView, PlaylistAddRemoveSongView, CollaborativePlaylistView,
    PodcastCreateView, PodcastDetailView,
    AlbumCreateView, AlbumDetailView,
    PremiumPlanCreateView, PremiumPlanDetailView,
)

urlpatterns = [
    path('artists/', ArtistListView.as_view(), name='artist-list'),
    path('songs/', SongListView.as_view(), name='song-list'),

    path('playlists/create/', PlaylistCreateView.as_view(), name='playlist-create'),
    path('playlists/<int:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),
    path('playlists/<int:pk>/update/', PlaylistAddRemoveSongView.as_view(), name='playlist-update'),
    path('playlists/<int:pk>/collaborators/', CollaborativePlaylistView.as_view(), name='collaborative-playlist'),

    path('podcasts/create/', PodcastCreateView.as_view(), name='podcast-create'),
    path('podcasts/<int:pk>/', PodcastDetailView.as_view(), name='podcast-detail'),

    path('albums/create/', AlbumCreateView.as_view(), name='album-create'),
    path('albums/<int:pk>/', AlbumDetailView.as_view(), name='album-detail'),

    path('premium-plans/create/', PremiumPlanCreateView.as_view(), name='premium-plan-create'),
    path('premium-plans/<int:pk>/', PremiumPlanDetailView.as_view(), name='premium-plan-detail'),
]
