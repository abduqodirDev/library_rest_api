from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from .models import Book
from yaml import serializer

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    # subtitle = serializers.CharField(validators=[UniqueValidator(queryset=Book.objects.all())])
    class Meta:
        model = Book
        fields = ("id", "title", "subtitle", "author", "isbn", "price")

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if not title.isalpha():
            raise ValidationError({
                "status": False,
                "message": "Iltimos titlega faqat harflar kiriting"
            })
        if Book.objects.filter(title=title).exists() and Book.objects.filter(author=author).exists():
            raise ValidationError({
                "status": False,
                "message": "Iltimos obyectni qayta qayta kiritmang"
            })
        return data

    def validate_price(self, price):
        if price <= 0 or price > 999999999:
            raise ValidationError({
                "status": False,
                "message": "Iltimos narxni to'g'ri kiriting!"
            })
        return price

# class BookSerializer(serializers.Serializer):
#     title = serializer.CharField(max_length=200)
#     subtitle = serializer.CharField(max_length=200)
#     author = serializers.CharField(max_length=200)
#     isbn = serializers.CharField(max_length=200)
#     price = serializers.DecimalField(max_digits=20, decimal_places=2)
