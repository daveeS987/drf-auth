from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MovieSerializer
from .models import Movie
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MovieList(ListCreateAPIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
