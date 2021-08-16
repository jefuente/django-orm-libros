from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    contexto={
        'books' : Book.objects.all(),
    }
    return render(request, 'index.html', contexto)

def crear_libro(request):
    print(request.POST)

    book = Book.objects.create(
        title  = request.POST['book_title'],
        desc  = request.POST['book_desc'],
        
    )

    return redirect('/')

def index2(request):
    contexto={
        'authors' : Author.objects.all(),
    }
    return render(request, 'index2.html', contexto)

   
def crear_autor(request):
    print(request.POST)

    author = Author.objects.create(
        first_name  = request.POST['first_name'],
        last_name  = request.POST['last_name'],
        notas  = request.POST['notas'],
    )

    return redirect('/authors')

def book(request, id):
    
    if request.method == 'GET':
        print(id)
        contexto = {
            'book': Book.objects.get(id=id),
            'autor': Author.objects.all()
        }
        return render(request, 'book.html',contexto)

    if request.method == 'POST':
        print(request.POST)
        book = Book.objects.get(id=id)
        this_author = Author.objects.get(id=request.POST['option'])
        book.authors.add(this_author)
        return redirect(f"/books/{id}")
 

def author(request, id):
    
    if request.method == 'GET':
        print(id)
        contexto = {
            'author': Author.objects.get(id=id),
            'book': Book.objects.all()
        }
        return render(request, 'author.html',contexto)

    if request.method == 'POST':
        print(request.POST)
        author = Author.objects.get(id=id)
        this_book = Book.objects.get(id=request.POST['option'])
        author.books.add(this_book)
        return redirect(f"/authors/{id}")

