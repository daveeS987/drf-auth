from rest_framework import generics
from .serializers import MovieSerializer
from .models import Movie
from .permissions import IsOwnerOrReadOnly


class MovieList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
