from django.shortcuts import render
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action
from .models import *
from .serializers import *

# Create your views here.



class ListSongsViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer


class AddAndUpdateSongsViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer


class DeleteSongsViewSet(mixins.DestroyModelMixin, GenericViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

    @action(detail=True, methods=['delete'])
    def custom_delete(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer()
        serializer.delete(instance)

        return Response(status=HTTP_204_NO_CONTENT)



    




