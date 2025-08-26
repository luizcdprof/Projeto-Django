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
    
    produto = "camisa"
    qtd = 2
    valor_unitario = 50
    valor_total = qtd * valor_unitario

    pedido = {
        'produto': produto,
        'qtd': qtd,
        'valor_unitario': valor_unitario,
        'valor_total': valor_total
    }

    produtos = [
        'maça',
        'laranja',
        'uva'
    ]

    return render(request, 'exibir.html', {'pedido': pedido, 'produtos': produtos})

def excluir(request):
    pass