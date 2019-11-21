class Quadrado:
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def __str__(self):
        return self.tamanho

    def mudarvalor(self, ntamanho):
        self.tamanho = ntamanho

    def retoralado(self, vtamanho):
        self.tamanho = vtamanho

    def calculoarea(self, gtamanho):
        area = gtamanho * gtamanho
        print(area)