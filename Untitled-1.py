class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} realizado. Novo saldo: R${self.saldo}')

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado. Novo saldo: R${self.saldo}')
        else:
            print('Saldo insuficiente.')

    def extrato(self):
        print(f'Extrato de {self.titular}: Saldo atual: R${self.saldo}')


# Exemplo de uso:
if __name__ == "__main__":
    conta = ContaBancaria("Fulano", 1000)
    conta.extrato()
    conta.deposito(500)
    conta.saque(200)
    conta.saque(1500)
    conta.extrato()

   