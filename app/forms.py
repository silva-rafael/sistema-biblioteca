from django import forms
from .models import Emprestimo, Devolucao, Livro, Aluno

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = '__all__'


class DevolucaoForm(forms.ModelForm):
    class Meta:
        model = Devolucao
        fields = '__all__'

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'