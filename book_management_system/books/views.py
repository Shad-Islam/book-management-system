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
    
def delete_book(request,book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('homepage')

def edit_book(request,book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BookForm(instance=book)
        return render(request,'add_book.html',{'form':form})
    
    
def view_book(request,book_id):
    book = Book.objects.get(id=book_id)
    return render(request,'view_book.html',{'book':book})