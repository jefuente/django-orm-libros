from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título")
    desc = models.TextField(verbose_name="Descripción")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #authors = autores del libro

    def __repr__(self):
        return f"{self.title}"
    def __str__(self):
        return f"{self.title}"

class Author(models.Model):
    first_name = models.CharField(max_length=45, verbose_name="Nombre")
    last_name = models.CharField(max_length=45, verbose_name="Apellido")
    notas = models.TextField(verbose_name="Notas")
    books = models.ManyToManyField(Book, related_name="authors", verbose_name="Libros")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

