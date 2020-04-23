from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
 
 
 
# Create your views here. 
def index(request): 

    allBooks = Book.objects.all()
    thisUser = User.object.get(id=request.session['cur_user'])

    context = {
        "allBooks" : allBooks,
        "user" : thisUser,
    }

    return render(request, 'books_app/index.html', context) 

def createBook(request):
    thisUser = User.objects.get(id=request.session['cur_user'])
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/books/')
    else:
        Book.objects.new_book(postData, thisUser)
        return redirect('/books/')

def favoriteThisBook(request, id):
    pass

def unFavoriteThisBook(request, id):
    pass



def thisBook(request, id):
    pass

def deleteBook(request, id):
    pass

def destroy(request):
    request.session.flush()
    return redirect('/')



