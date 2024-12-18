from django.contrib import admin
from .models import Aluno, Emprestimo, Devolucao, Livro

admin.site.register(Aluno)
admin.site.register(Livro)
admin.site.register(Emprestimo)
admin.site.register(Devolucao)
