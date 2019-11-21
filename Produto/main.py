from produto_regra import ProdutoRegra

def mostrar_menu():
    print('1 - Cadastrar')
    print('2 - Vizualizar')
    print('0 - Sair')

    opcao = -1
    
    try:
        opcao = int(input("Informe uma opção: "))
    except ValueError:
        print('Valor informado deve ser um número!')
        return 0

    if opcao > 2 or opcao < 0:
        print('Opcão inválida! ')      
        return 0   

    return opcao

def main():

    produto_regra = ProdutoRegra()

    opcao_retornada = -1

    while opcao_retornada != 0:
    
        opcao_retornada = mostrar_menu()

        if opcao_retornada == 1:
            produto_regra.cadastrar()
        elif opcao_retornada == 2:
            print('Escolheu a opção 2')
        else:
            print('Escolheu a opção 0')
                

main()    

