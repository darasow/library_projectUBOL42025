from django.urls import path
from . import views
app_name = 'publishers'

urlpatterns = [
    path('', views.publisher_list, name='publisher_list'),
    path('<int:id>/', views.publisher_detail, name='publisher_detail')
]