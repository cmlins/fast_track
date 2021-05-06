url = 'bytebank.com/cambio?moedaOrigem=real'
print(url)

url_base = url[0:19]
print(url_base)

url_param = url[20:]
print(url_param)

print('\n###\n')

url2 = 'bytebank.com/cambio?moedaOrigem=real'
print(url2)

indice_interrogacao = url2.find('?')

url2_base = url2[0:indice_interrogacao]
print(url2_base)

url2_param = url2[indice_interrogacao:]
print(url2_param)

print('\n###\n')

nome_completo = 'Gabriel Saldanha'
nome = nome_completo[:7]
sobrenome = nome_completo[8:]
print(len(nome_completo))
print(nome)
print(sobrenome)

print('\n###\n')

url3 = 'bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'

indice_interrogacao = url3.find('?')
url3_base = url3[0:indice_interrogacao]
url3_param = url3[indice_interrogacao+1:]

param = 'moedaOrigem'
# param = 'moedaDestino'
indice_param = url3_param.find(param)
len_param = len(param)


indice_valor = indice_param + len_param + 1
indice_e_comercial = url3_param.find('&', indice_valor)

if(indice_e_comercial == -1):
    valor = url3_param[indice_valor:]
else:
    valor = url3_param[indice_valor:indice_e_comercial]

print(valor)

print('\n###\n')


