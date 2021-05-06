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
        

url = 'bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'
extrator_url = ExtratorURL(url)
valor = extrator_url.get_valor_param('moedaDestino')
print(valor)

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url2 = ExtratorURL(url)
valor_quantidade = extrator_url2.get_valor_param("quantidade")
print(valor_quantidade)




