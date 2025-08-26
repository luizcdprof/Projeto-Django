from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='usuario_cadastrar'),
    path('login/', views.login, name='usuario_login'),
    path('logout/', views.logout, name='usuario_logout'),
    path('atualizar/', views.atualizar, name='usuario_atualizar'),
    path('exibir/', views.exibir, name='usuario_exibir'),
    path('excluir/', views.excluir, name='usuario_excluir'),
]