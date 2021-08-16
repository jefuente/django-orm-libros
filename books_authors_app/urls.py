from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('crear_libro', views.crear_libro),
    path('authors', views.index2),
    path('crear_autor', views.crear_autor),
    path('books/<int:id>', views.book),
    path('authors/<int:id>', views.author),
    
]




