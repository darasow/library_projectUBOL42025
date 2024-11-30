from django.urls import path
from . import views
app_name = 'staff'

urlpatterns = [
path('register/', views.register, name='register'), # Inscription
path('profile/', views.profile, name='profile'), # Modification du profil
path('login/', views.user_login, name='login'),
path('', views.user_login, name='login'),
path('logout/', views.user_logout, name='logout'),
]