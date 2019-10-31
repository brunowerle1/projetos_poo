#Importando a classe que será utilizada
#para criar os objetos 
from pessoa import Pessoa
from veiculo import Veiculo

def main():
    print('Meu primeiro programa orientado a objetos!')


        # Instãnciando um novo objeto a partir 
        # da Classe Pessoa e armazenando a instancia na variavel pessoa1
    pessoa1 = Pessoa()
    print(type(pessoa1))

    pessoa1.nome = 'Bruno'
    pessoa1.sexo = 'Masculino'
    pessoa1.idade = 19
    print(pessoa1)
    print('Nome: {}'.format(pessoa1.nome)) 
    print('Idade: {}'.format(pessoa1.idade))
    print('Sexo: {}'.format(pessoa1.sexo))

    print(pessoa1.imprimir())

    #Instanciando um objeto a partir da classe veiculo, cujo construtor foi sobrescrito
    veiculo = Veiculo('Gol' ,'VW' , 'Branca' , '1997')
    print('Nome do veiculo:',veiculo.nome)

main()