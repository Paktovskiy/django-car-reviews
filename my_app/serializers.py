from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField, StringRelatedField
from .models import Country, Manufacturer, Car, Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author_email', 'car', 'created_at', 'comment']

    def validate_author_email(self, value):
        if not value.endswith("@example.com"):
            raise ValidationError("Допустимы только email-адреса с доменом @example.com")
        return value


class CarSerializer(ModelSerializer):
    manufacturer = StringRelatedField()
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'name', 'manufacturer', 'comments', 'comment_count']

    def get_comment_count(self, obj):
        return obj.comments.count()


class ManufacturerSerializer(ModelSerializer):
    country = StringRelatedField()
    cars = StringRelatedField(many=True, read_only=True)
    comments_count = SerializerMethodField()

    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country', 'cars', 'comments_count']

    def get_comments_count(self, obj):
        return Comment.objects.filter(car__manufacturer=obj).count()


class CountrySerializer(ModelSerializer):
    manufacturers = StringRelatedField(many=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'manufacturers']
