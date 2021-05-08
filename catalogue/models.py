from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    auth_name=models.CharField(max_length=50)
    date_of_birth=models.DateField(max_length=15)
    date_of_death=models.DateField(max_length=15)

    def __str__(self):
        return self.auth_name


class Language(models.Model):
    lang_name=models.CharField(max_length=50)
    def __str__(self):
        return self.lang_name

class Genre(models.Model):
    genre_name=models.CharField(max_length=50)
    def __str__(self):
        return self.genre_name

class BookIbstance(models.Model):
    status=models.CharField(max_length=20)
    imprint=models.CharField(max_length=200)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)

class Book(models.Model):
    title=models.CharField(max_length=50)
    summary=models.CharField(max_length=50)
    isbn=models.CharField(max_length=50)
    genre=models.ForeignKey(Genre, on_delete=models.SET_NULL ,null=True)
    language=models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    author=models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title