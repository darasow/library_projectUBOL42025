from django.urls import path

from . import views
from library_project import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
app_name = 'authors'

urlpatterns = [
    path('', login_required(views.author_list), name='author_list'),
    path('<int:id>/', views.author_detail, name='author_detail'),
    path('add_author/', views.add_author, name='add_author'),
    # Supprimer un auteur
    path('delete_author/<int:id>/', views.delete_author, name='delete_author'),
    # Mettre à jour un auteur
    path('update_author/<int:id>/', views.update_author, name='update_author'),
]

if settings.DEBUG:  # Servir les fichiers médias seulement en mode debug
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)