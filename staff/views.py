from django.shortcuts import redirect, render

from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user) # Connecte l'utilisateur
            messages.success(request, "Vous êtes maintenant connecté.")
            return redirect('/authors/') # Remplacez ‘authors’ par l'URL vers laquelle vous voulez rediriger
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
      form = LoginForm()
    return render(request, 'staff/login.html', {'form': form})

def user_logout(request):
    logout(request) # Déconnecte l'utilisateur
    messages.success(request, "Vous avez été déconnecté.")
    return redirect('/staff/login') # Remplacez 'home' par l'URL vers laquelle vous voulez rediriger


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a été créé avec succès!")
        return redirect('staff:login') # Redirige l'utilisateur vers la page de connexion après l'inscription
    else:
       form = RegistrationForm()
    return render(request, 'staff/register.html', {'form': form})

def profile(request):
    pass
