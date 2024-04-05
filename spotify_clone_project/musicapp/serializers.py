from rest_framework import serializers
# from .models import Artist, Song, Podcast, Playlist, Album, Blend, PremiumPlan
from .models import *

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        
        
    def validate_likes(self, value):
        if value < 0:
            raise serializers.ValidationError("Likes count cannot be negative.")
        return value

    def validate_downloads(self, value):
        if value < 0:
            raise serializers.ValidationError("Downloads count cannot be negative.")
        return value
    
     # Custom method to count the number of likes for a song
    def get_likes_count(self, obj):
        return obj.likes

    # Custom method to count the number of songs for an artist
    def get_songs_count(self, obj):
        return obj.artist.song_set.count()

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
        
    
    def validate_songs(self, value):
        if value.count() < 1:
            raise serializers.ValidationError("A playlist must have at least 1   songs.")
        return value

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class BlendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blend
        fields = '__all__'

class PremiumPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumPlan
        fields = '__all__'
