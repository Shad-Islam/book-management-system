from django.shortcuts import render
from .models import Book

# Create your views here.
def homepage(request):
    books = Book.objects.all()
    return render(request,'book-list.html',{'books':books})
   