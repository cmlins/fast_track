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

    def __pode_sacar(self, valor):
        disponivel_para_saque = self.__saldo + self.__limite
        return valor <= disponivel_para_saque

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou do limite')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}

    @limite.setter
    def limite(self, limite):
        self.__limite = limite



conta1 = Conta(123, 'Nemo', 100.0, 100.0)
conta2 = Conta(234, 'Dory', 1000.0, 2000.0)

print('\nSaca')
conta1.saca(1500)
conta1.extrato()

print('\nDeposita')
conta1.deposita(300)
conta1.extrato()

print('\nTransfere')
conta2.transfere(300, conta1)
conta1.extrato()

print('\nLimite')
conta1.limite = 10000.0
print(conta1.limite)

print('\nCódigo banco')
print(conta1.codigo_banco())
print(Conta.codigo_banco())

print('\nCódigos bancos')
print(conta1.codigos_bancos()['Caixa'])



