class Pessoa:
    #Atributos
    nome = ''
    idade = 0
    sexo = ''

    # Metodos
    # self representa sua propria classe
    def imprimir(self):
        return self.nome + ' - ' + str(self.idade) + ' - ' + self.sexo
