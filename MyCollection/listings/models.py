from django.db import models
from Authentication.models import User


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.fields.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    price = models.fields.FloatField(null=True)
    author = models.fields.CharField(max_length=100)

    def __str__(self):
        return self.name

    @staticmethod
    def calculate_total_price(user):
        books = Book.objects.filter(user=user)
        total_price = sum(book.price for book in books if book.price is not None)
        return total_price
