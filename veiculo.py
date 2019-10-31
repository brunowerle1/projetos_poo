class Veiculo:

    # Declarando o método construtor
    def __init__(self, nome, marca, cor, ano):
        self.nome = nome 
        self.marca = marca
        self.cor = cor
        self.ano = ano

# Sobrescrevendo o metodo str




    def __str__(self):
        return self.nome + ' - ' + self.marca + ' - ' + self.cor + ' - ' + str(self.ano)
        