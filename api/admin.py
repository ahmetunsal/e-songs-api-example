from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ['song_name', 'song_artist', 'song_album', 'song_relase_date']



