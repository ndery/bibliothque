from django.contrib import admin
from .models import Book , BookIbstance, Genre, Language, Author


admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(BookIbstance)
admin.site.register(Language)
admin.site.register(Author)
# Register your models here.
