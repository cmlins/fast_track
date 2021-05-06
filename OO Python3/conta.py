class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f'Contruindo objeto ... {self}')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'Saldo é {self.saldo} do titular {self.titular}.')

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor


conta = Conta(123, 'Nemo', 100.0, 100.0)
print(conta.titular)
conta.extrato()
conta.saca(15)
conta.extrato()
conta.deposita(300)
conta.extrato()
