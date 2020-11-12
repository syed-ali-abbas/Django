from django.db import models
from rest_framework import serializers


class Book(models.Model):
    bk_name = models.CharField(max_length=100)
    bk_prize = models.IntegerField()
    bk_pages = models.IntegerField()

    def __str__(self):
        return self.bk_name

    
    def AlLBooks():
        return Book.objects.all()


class BookSerializer(serializers.Serializer):
    bk_name = serializers.CharField(max_length=100)
    bk_prize = serializers.IntegerField()
    bk_pages = serializers.IntegerField()
    id = serializers.IntegerField()


