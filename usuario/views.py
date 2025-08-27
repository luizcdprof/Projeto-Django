from django.shortcuts import render, redirect

# Create your views here.
def cadastrar(request):
    return render(request, 'cadastrar.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    logout()
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