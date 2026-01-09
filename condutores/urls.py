from django.urls import path
from . import views

urlpatterns = [
    path('', views.condutor_list, name='condutor_list'),
    path('avaliar/<int:pk>/', views.condutor_avaliar, name='condutor_avaliar'),
    path('novo/', views.condutor_create, name='condutor_create'),
    path('<int:id>/editar/', views.condutor_update, name='condutor_update'),
    path('<int:id>/excluir/', views.condutor_delete, name='condutor_delete'),
]