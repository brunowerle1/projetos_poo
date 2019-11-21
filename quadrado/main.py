from quadrado import Quadrado

def main():
    tamanho = float(input("Informe o tamanho: "))
    quadrado = Quadrado(tamanho)
    print("Informe 1 para mudar o lado")
    print("Informe 2 para retornar o valor do lado")
    print("Informe 3 para retornar o calculo da area")
    escolha = input("Informe sua decisao")
    while escolha != '0':
        if escolha == '1':
            valor = input("Informe novo valor")
            quadrado.mudarvalor(valor)
            print(valor)
            break
        elif escolha == '2':
            quadrado.retoralado(tamanho)
            print(tamanho)
            break
        elif escolha == '3':
            quadrado.calculoarea(tamanho)
            break

main()