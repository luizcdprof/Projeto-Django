from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('usuario_login')

def atualizar(request):
    pass

def exibir(request):
    #  Buscar no banco de dados o usuario atual
    
    pedidos = {
        '123': {'produto': 'camiseta', 'qtd': 2, 'valor': 49.99, 'total': 99.98},
        '456': {'produto': 'calça', 'qtd': 1, 'valor': 99.99, 'total': 99.99},
        '789': {'produto': 'tênis', 'qtd': 1, 'valor': 199.99, 'total': 199.99},
    }

    return render(request, 'exibir.html', {'pedidos': pedidos})

def excluir(request):
    pass