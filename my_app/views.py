from rest_framework.viewsets import ModelViewSet
from .models import Country, Manufacturer, Car, Comment
from .serializers import CountrySerializer, ManufacturerSerializer, CarSerializer, CommentSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny


class BaseViewSet(ModelViewSet):
    permitted_methods = ['GET']

    def get_permissions(self):
        if self.request.method in self.permitted_methods:
            return [AllowAny()]
        return [IsAuthenticated()]


class CountryViewSet(BaseViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ManufacturerViewSet(BaseViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CarViewSet(BaseViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CommentViewSet(BaseViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permitted_methods = ['GET', 'POST']