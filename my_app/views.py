from rest_framework.viewsets import ModelViewSet
from .models import Country, Manufacturer, Car, Comment
from .serializers import CountrySerializer, ManufacturerSerializer, CarSerializer, CommentSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [AllowAny()]
        return [IsAuthenticated()]


class ManufacturerViewSet(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [AllowAny()]
        return [IsAuthenticated()]


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [AllowAny()]
        return [IsAuthenticated()]


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'GET']:
            return [AllowAny()]
        return [IsAuthenticated()]
