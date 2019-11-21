class Bola:
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def __str__(self):
        return self.cor + ' - ' + self.circuferencia + ' - ' + self.material    

    
    def trocacor(self, ncor):
        self.cor = ncor

    def mostracor(self, cor):
        print (self.cor)