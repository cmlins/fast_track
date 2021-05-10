from forca import Forca
from adivinhacao import Adivinhacao

def escolhe_jogo():
    print('''
    ********************************
    *******Escolha o seu jogo*******
    ********************************
    ''')

    print('(1) Forca\n(2) Adivinhação\n')

    jogo = int(input('Qual o jogo?'))

    if(jogo == 1):
        print('Jogo da Forca')
        Forca.jogar_forca()
    elif(jogo == 2):
        print('Jogo da Adivinhação')
        Adivinhacao.jogar_adivinhacao()

if(__name__ == '__main__'):
    escolhe_jogo()