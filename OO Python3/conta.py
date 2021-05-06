import os
os.system('cls' if os.name == 'nt' else 'clear')

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto ... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)



conta1 = Conta(123, 'Nemo', 100.0, 100.0)
conta2 = Conta(234, 'Dory', 1000.0, 2000.0)
conta1.extrato()
conta1.saca(15)
conta1.extrato()
conta1.deposita(300)
conta2.transfere(300, conta1)
conta1.extrato()
