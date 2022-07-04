# from django.http import JsonResponse
from django.shortcuts import redirect, render
from livro.forms import LivroForm
from livro.models import Livros


def home(request):
    data= {}
    data['db'] = Livros.objects.all()
    return render(request, 'index.html', data)

def form(request):
     data = {}
     data['form'] = LivroForm
     return render(request, 'form.html', data)


def create (request):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data ={}
    data['db'] = Livros.objects.get(pk=pk)
    return render(request, 'view.html', data)



def edit(request, pk):
    data ={}
    data['db']= Livros.objects.get(pk=pk)
    data['form'] = LivroForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data ={}
    data['db']= Livros.objects.get(pk=pk)
    form = LivroForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Livros.objects.get(pk=pk)
    db.delete()
    return redirect('home')

# Retornando json
# def livro(request):
#     if request.method == 'GET':
#         livro = {
#                 'id': 1,
#                 'nome': 'A maldicao do tigre',
#                 'autora': 'Colleen Houck'
#         }
#         return JsonResponse(livro)


