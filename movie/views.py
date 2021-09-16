from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MovieSerializer
from .models import Movie
from .permissions import IsOwnerOrReadOnly


class MovieList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
