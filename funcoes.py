
def menu():
    
    selecao = input(
        
        '''
        SELECIONE A OPÇÃO DESEJADA
        
        1-------- CADASTRAR PRODUTOS
        1.1------ VISUALIZAR PRODUTOS
        2-------- CADASTRAR CLIENTE
        2.1------ VISUALIZAR CLIENTES
        3-------- EFETUAR VENDAS
        3.1------ VISUALIZAR VENDAS
        
        '''
    )
    
    if selecao == "1":
        cadastroProduto()
    elif selecao =="1.1":
        mostraProduto()
    elif selecao == "2":
        cadastroCliente()
    elif selecao == "2.1":
        mostraCliente()
    elif selecao == "3":
        venda()
    else:
        mostrarVenda()
        

def cadastroProduto():
    nome  =  input("Digite o nome do produto     :       ")
    ean   =  input("Digite o GTIN/EAN            :       ")
    valor =  input("Digite o valor do            :       ")

def mostraProduto():
    print(f'Ver Produtos')

def cadastroCliente():
    return print(f'Cadastrar Cliente')

def mostraCliente():
    return print(f'Vizualizar Clientes Cadastrados')

def venda():
    return print(f'Realizar Vendas')

def mostrarVenda():
    return print(f'Visualizar Vendas')

def main():
    
    menu()

main()