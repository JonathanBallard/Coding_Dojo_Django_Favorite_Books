from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index), 
    path('destroy/', views.destroy), 
    path('books/create/', views.createBook), 
    path('books/<int:id>/', views.thisBook), 
    path('books/delete/<int:id>/', views.deleteBook), 
    path('books/favorite/<int:id>/', views.favoriteThisBook), 
    path('books/unfavorite/<int:id>/', views.unFavoriteThisBook), 

] 
