import forca
import adivinhacao

def escolhe_jogo():
    print('''
    ********************************
    *******Escolha o seu jogo*******
    ********************************
    ''')

    print('(1) Forca\n(2) Adivinhação\n')

    jogo = int(input('Qual o jogo? '))

    if(jogo == 1):
        print('\nJogo da Forca')
        forca.jogar_forca()
    elif(jogo == 2):
        print('\nJogo da Adivinhação')
        adivinhacao.jogar_adivinhacao()

if(__name__ == '__main__'):
    escolhe_jogo()