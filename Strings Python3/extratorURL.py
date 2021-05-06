import re

class ExtratorURL:

    def __init__(self, url)    :
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if(type(url) == str):
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if(not self.url):
            raise ValueError('A URL está vazia')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError('A URL não é válida!')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_param(self):
        indice_interrogacao = self.url.find('?')
        url_param = self.url[indice_interrogacao+1:]
        return url_param

    def get_valor_param(self, param):
        indice_param = self.get_url_param().find(param)
        len_param = len(param)


        indice_valor = indice_param + len_param + 1
        indice_e_comercial =  self.get_url_param().find('&', indice_valor)

        if(indice_e_comercial == -1):
            valor =  self.get_url_param()[indice_valor:]
        else:
            valor =  self.get_url_param()[indice_valor:indice_e_comercial]

        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\n' + 'Parâmetros: ' + self.get_url_param() + '\n' + 'URL base: ' + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url
        

url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real'
extrator_url = ExtratorURL(url)
# print(f'O tamanho da URL: {len(extrator_url)}')
# print(extrator_url)
moeda_origem = extrator_url.get_valor_param('moedaOrigem')
moeda_destino = extrator_url.get_valor_param('moedaDestino')
quantidade = extrator_url.get_valor_param('quantidade')

VALOR_DOLAR = 5.5
print(moeda_origem)
print(moeda_destino)
print(quantidade)

if(moeda_origem == 'real' and moeda_destino == 'dolar'):
    converte = int(quantidade) / VALOR_DOLAR
    print(f'R$ {quantidade} reais equivale a $ {str(converte)} reais.')
elif(moeda_origem == 'dolar' and moeda_destino == 'real'):
    converte = int(quantidade) * VALOR_DOLAR
    print(f'$ {quantidade} dólares equivale a R$ {str(converte)} reais.')
else:
    print(f'Câmbio de {moeda_origem} para {moeda_destino} não está disponível.')



