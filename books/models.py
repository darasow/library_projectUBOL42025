from django.db import models

from authors.models import Author
from publishers.models import Publisher

class ISBN(models.Model):
        code = models.CharField(max_length=20)
        # ISBN est composé de 20 caractères
        def __str__(self):
           return self.code
        

class Book(models.Model):
    title = models.CharField(max_length=200)
    # Le titre du livre
    publication_date = models.DateField()
    # La date de publication
    summary = models.TextField()
    # Résumé du livre
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # ForeignKey, plusieurs livres peuvent avoir un même auteur
    isbn = models.OneToOneField(ISBN, on_delete=models.CASCADE)
    # OneToOneField, chaque livre a un ISBN unique
    publishers = models.ManyToManyField(Publisher)
    # ManyToManyField, un livre peut avoir plusieurs éditeurs
def __str__(self):
    return self.title