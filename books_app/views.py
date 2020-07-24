from django.shortcuts import render, redirect
from . import models
# Create your views here.


def index(request):
    context = {
        'books': models.Book.objects.all()
    }
    return render(request, 'index.html', context)


def add_book(request):
    models.Book.objects.create(
        title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')


def show_book(request, id):
    book = models.Book.objects.get(id=id)
    context = {
        'book': models.Book.objects.get(id=id),
        'authors': models.Author.objects.all()
    }

    return render(request, 'book.html', context)


def add_author_to_book(request, id):
    author_to_add = models.Author.objects.get(
        id=request.POST['author_from_select'])
    book_selected = models.Book.objects.get(id=id)
    author_to_add.books.add(book_selected)
    return redirect(f'/show_book/{id}')
