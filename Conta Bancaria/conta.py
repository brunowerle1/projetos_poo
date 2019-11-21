from movimentacao import Movimentacao
import datetime

class Conta:
    agencia = 0
    numero = 0
    saldo = 0
    cliente = None
    movimentacoes = []

    def depositar(self, valor):
        self.saldo += valor
        # Para cada depósito gera um novo objeto
        # movimentacao, com os dados da movimentação
        mov_deposito = Movimentacao(datetime.datetime.now(), valor, self, 1)
        # Após gerar o novo movimento, ele é
        # armazenado no atributo movimentacoes
        self.movimentacoes.append(mov_deposito)
        print(f'Depósito de {valor} efetuado com sucesso!')

    def sacar(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            mov_saque = Movimentacao(datetime.datetime.now(), valor, self, 2)
            self.movimentacoes.append(mov_saque)
            print(f'Saque de {valor} efetuado com sucesso!')
        else:
            print('Saldo insuficiente!')
