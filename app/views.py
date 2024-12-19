from django.shortcuts import render, redirect
from .forms import EmprestimoForm, DevolucaoForm, LivroForm, AlunoForm

def index(request):
    return render(request, 'app/index.html')

def livros(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LivroForm()
    return render(request, 'app/create_livro.html', {'form':form})

def alunos(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlunoForm()
    return render(request, 'app/create_aluno.html', {'form':form})

def emprestimos(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmprestimoForm()
    return render(request, 'app/create_emprestimo.html', {'form':form})

def devolucoes(request):
    if request.method == 'POST':
        form = DevolucaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DevolucaoForm()
    return render(request, 'app/create_devolucao.html', {'form':form})