import random

def jogar_forca():

    msg_abertura()

    palavra = palavra_secreta()

    acertos = campos_da_forca(palavra)

    erros = 0
    
    while(True):
        chute = pede_chute()

        if(chute in palavra):
            index = 0
            for letra in palavra:
                if(letra == chute):
                    acertos[index] = letra
                    # print(f'A letra "{chute}" está na posição "{index}" da palavra!')
                    acertou = True
                index += 1
        else:
            erros += 1
            desenha_forca(erros)

        if(erros == 7):
            break
        if('_' not in acertos):
            break

        print(acertos, '\n')
        print(f'\nVocê ainda tem mais {6-erros} tentativas\n')

    if('_' not in acertos):
        msg_ganhador()
    else:
        msg_perdedor(palavra)
    print('\nEndgame\n')

def msg_perdedor(palavra):
    print("\nPuxa, você foi enforcado!")
    print(f"A palavra era {palavra}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def msg_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def pede_chute():
    return input('Qual a letra? ').strip().upper()

def campos_da_forca(palavra):
    acertos = ['_' for letra in range(len(palavra))]
    print(acertos, '\n')
    return acertos

def msg_abertura():
    print('''
    ********************************
    ***Bem vindo ao jogo de forca***
    ********************************
    ''')

def palavra_secreta():
    # Captura das palavras do jogo em um arquivo para que possa ser escolhida uma aleatoriamente
    arquivo = open('python_p2\jogos\palavras.txt', 'r')

    palavras = [linha.strip() for linha in arquivo]

    arquivo.close()

    num = random.randrange(0, len(palavras))
    palavra = palavras[num].upper()
    return palavra

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == '__main__'):
    jogar_forca()
