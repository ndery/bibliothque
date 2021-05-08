from django.urls import path
from .views import index , book_list

urlpatterns=[
    path("", index , name='index'),
    path("catalog", book_list ,name='catalog'),
]