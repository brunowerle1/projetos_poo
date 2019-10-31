class Conta:
    agencia = 0
    numero = 0
    saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de {valor} efetuado com sucesso!')

    def sacar(self, valor):
        self.saldo -= valor
        print(f'Saque de {valor} efetuado com sucesso!')