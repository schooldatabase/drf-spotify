from django.contrib import admin
from .models import Artist, Song, Podcast, Playlist, Album, Blend, PremiumPlan

# class SongInline(admin.TabularInline):
#     model = Song
#     extra = 1

# class ArtistAdmin(admin.ModelAdmin):
#     inlines = [SongInline]

#     list_display = ['id', 'name', 'performed_by', 'written_by', 'produced_by']  # Add other fields as needed

admin.site.register(Artist)


admin.site.register(Song)
admin.site.register(Podcast)
admin.site.register(Playlist)
admin.site.register(Album)
admin.site.register(Blend)
admin.site.register(PremiumPlan)
