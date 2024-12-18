from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    responsavel = models.CharField(max_length=100, blank=True, null=True)
    rua = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=5, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=200, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=10, blank=True, null=True)
    ano = models.CharField(max_length=4, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
class Emprestimo(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    livro = models.ManyToManyField(Livro)
    observacao = models.TextField(blank=True, null=True)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Emprestado para {self.aluno.nome}'


class Devolucao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    livro = models.ManyToManyField(Livro)
    observacao = models.TextField(blank=True, null=True)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Aluno - {self.aluno.nome}'
 
