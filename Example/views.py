from rest_framework import generics
from .serializers import ExampleSerializer
from .models import Example
from .permissions import IsOwnerOrReadOnly


class ExampleList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer


class ExampleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
