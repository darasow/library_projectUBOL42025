import os
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404
from faker import Faker

from authors.forms import AuthorForm

from .models import Author
# Create your views here.


def author_list(request):
    authors = Author.objects.all().order_by('-created_at')
    return render(request, 'authors/author_list.html', {'authors': authors})

def author_detail(request, id):
    author = get_object_or_404(Author, pk=id)
    return render(request, 'authors/author_detail.html', {'author': author})

fake = Faker()# Initialiser Faker
# def add_author(request):
#     author = Author(
#     name=fake.name(), # Générer un nom factice
#     birthdate=fake.date_of_birth(),# Générer une date de naissance factice
#     biography=fake.text() # Générer une biographie factice
#     )
#     author.save()
#     return HttpResponseRedirect('/authors/')
def add_author(request):
    if request.method == 'POST':
      form = AuthorForm(request.POST, request.FILES)
      if form.is_valid():
        form.save() # Enregistre directement l'auteur en base de données
        return redirect('authors:author_list')
    else:
       form = AuthorForm()
    return render(request, 'authors/author_form.html', {'form': form})


def delete_author(request, id):
    author = get_object_or_404(Author, id=id)
    author.delete()
    return HttpResponseRedirect('/authors/')

# Mettre à jour un auteur avec des données factices via Faker
# def update_author(request, id):
#     author = get_object_or_404(Author, id=id)
#     author.name = fake.name() # Nouveau nom factice
#     author.birthdate = fake.date_of_birth() # Nouvelle date de naissanc factice
#     author.biography = fake.text() # Nouvelle biographie factice
#     author.save()
#     return HttpResponseRedirect('/authors/')

def update_author(request, id):
    author = get_object_or_404(Author, id=id)
    old_image_path = author.image.path if author.image else None
    if request.method == 'POST':
    # Liaison avec l'instance existante
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            if 'image' in request.FILES:
                # Supprime l'ancienne image si elle existe
                if old_image_path and os.path.isfile(old_image_path):
                    os.remove(old_image_path)
            form.save() # Met à jour l'auteur existant
            return redirect('authors:author_list')
    else:
        # Pré-remplissage pour la modification
        form = AuthorForm(instance=author)
        return render(request,'authors/author_form.html',{'form': form})