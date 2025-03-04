from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm

# Create your views here.
def homepage(request):
    books = Book.objects.all()
    return render(request,'book_list.html',{'books':books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('homepage')
    else:
        print('get the form') 
        form = BookForm()
        return render(request,'add_book.html', {'form':form})