from rest_framework import viewsets, generics
from myflix.serializers import userSerializer, streamSerializer, listaSerializer, listaStreamSerializer, listaUserSerializer
from myflix.models import user, stream, lista

class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer

class streamViewSet(viewsets.ModelViewSet):
    queryset = stream.objects.all()
    serializer_class = streamSerializer

class listaViewSet(viewsets.ModelViewSet):
    queryset = lista.objects.all()
    serializer_class = listaSerializer

class listaUser(generics.ListAPIView):
    def get_queryset(self):
        queryset = lista.objects.filter(user_id=self.kwargs['pk'])
        return queryset
    serializer_class = listaUserSerializer

class listaStream(generics.ListAPIView):
    def get_queryset(self):
        queryset = lista.objects.filter(stream_id=self.kwargs['pk'])
        return queryset
    serializer_class = listaStreamSerializer