from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('livros/', views.livros, name='livros'),
    path('emprestimos/', views.emprestimos, name='emprestimos'),
    path('devolucoes/', views.devolucoes, name='devolucoes'),
    path('alunos/', views.alunos, name='alunos'),

]