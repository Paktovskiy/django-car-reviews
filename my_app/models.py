from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='manufacturers')

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='cars')
    production_start_year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2024)])
    production_end_year = models.PositiveIntegerField(null=True, blank=True,
                                                      validators=[MinValueValidator(1900), MaxValueValidator(2024)])

    def __str__(self):
        return self.name


class Comment(models.Model):
    author_email = models.EmailField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return f"Comment by {self.author_email} on {self.car}"
