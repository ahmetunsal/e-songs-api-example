from django.db import models
from django.utils import timezone

# Create your models here.



class Songs(models.Model):
    song_name = models.CharField(max_length=200)
    song_artist = models.CharField(max_length=200)
    song_album = models.CharField(max_length=200)
    song_relase_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.song_artist} => {self.song_name}'




