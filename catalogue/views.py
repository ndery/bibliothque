from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Book
# Create your views here.
@login_required
def index(request):
  return render(request, 'index.html')


@login_required
def book_list(request):
      
  user = request.user
  books=Book.objects.all
  
  return render(request, 'catalog.html', {'books':books})


