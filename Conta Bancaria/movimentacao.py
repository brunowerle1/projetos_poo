class Movimentacao:
    data = None
    valor = 0
    conta = None
    tipo = 0 # 1 - Depósito / 2 - Saque

    def __init__(self, data, valor, conta, tipo):
        self.data = data
        self.valor = valor
        self.conta = conta
        self.tipo = tipo