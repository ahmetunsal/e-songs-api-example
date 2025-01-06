from rest_framework.serializers import ModelSerializer
from api.models import * 




class SongsSerializer(ModelSerializer):
    class Meta:
        model = Songs
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

        def create(self, validated_data):
            isinstance = Songs.objects.create(**validated_data)
            return isinstance
        

        def update(self, instance, validated_data):
            instance.song_name = validated_data.get('song_name', instance.song_name)
            instance.song_artist = validated_data.get('song_artist', instance.song_artist)
            instance.song_album = validated_data.get('song_album', instance.song_album)
            instance.song_relase_date = validated_data.get('song_relase_date', instance.song_relase_date)

            instance.save()

            return instance
        

        def delete(self, instance):
            instance.delete()
            return None




