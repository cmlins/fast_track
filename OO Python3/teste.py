def cria_conta(numero, titular, saldo, limite):
    conta = {
        "numero": numero,
        "titular": titular,
        "saldo": saldo,
        "limite": limite
    }
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print(f'Saldo é {conta["saldo"]}')


conta1 = cria_conta(123, 'nemo', 100.0, 100.0)
deposita(conta1, 100)
extrato(conta1)
saca(conta1, 150)
extrato(conta1)

