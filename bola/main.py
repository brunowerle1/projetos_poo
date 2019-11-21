from bola import Bola

def main():
    cor = input("Informe a cor da bola :")
    circuferencia = input("Informe a circuferencia da bola :")
    material = input("Informe o material da bola :")
    bola = Bola(cor, circuferencia, material)
    print(bola)
    print("Informe 1 para trocar a cor !")
    print("Informe 2 para mostrar a cor !")
    escolha = input("Informe sua escolha !")
    while escolha !=  '0':
        if escolha == '1':
            cor = input("Informe a nova cor :")
            bola.trocacor(cor)
            print(cor)
            break
        elif escolha == '2':
            bola.mostracor(cor)
            break

main()