import random
class Adivinhacao:

    def jogar_adivinhacao():
        print('''
        ********************************
        Bem vindo ao jogo de adivinhação
        ********************************
        ''')

        num_secreto = random.randrange(1,101)
        # print(num_secreto)
        tentativas = 0
        pontos = 1000

        print('''
        Qual o nível de dificuldade?
        (1) Fácil (2) Média (3) Difícil
        ''')

        nivel = int(input('Defina o nível: '))

        if(nivel == 1):
            tentativas = 20
        elif(nivel == 2):
            tentativas = 10
        else:
            tentativas = 5

        total_tentativas = tentativas
        rodada = 1
        # while(tentativas > 0):
        for rodada in range (1, total_tentativas+1):
            print(f'\nTentativa {rodada} de {total_tentativas}')

            chute = int(input('Digite um número entre 1 e 100: '))

            print('Você digitou', chute)

            if(chute < 1 or chute > 100):
                print('Digite um número entre 1 e 100!')
                continue
            else:
                acerto = num_secreto == chute
                maior = num_secreto < chute
                menor = num_secreto > chute

                if(acerto):
                    print(f'Acertasse!!! Fizesse {pontos} pontos!')
                    break
                else:
                    if(maior):
                        print('Errasse! Seu chute foi maior que o número')
                        if(rodada == total_tentativas):
                            print(f'O número secreto era {num_secreto}. Você fez {pontos} pontos!')
                    elif(menor):
                        print('Errasse! Seu chute foi menor que o número')
                        if(rodada == total_tentativas):
                            print(f'O número secreto era {num_secreto}. Você fez {pontos} pontos!')
                    pontos_perdidos = abs(num_secreto - chute)
                    pontos = pontos - pontos_perdidos

            tentativas -= 1
            rodada += 1

        print('\nEndgame\n')

    if(__name__ == '__main__'):
        jogar_adivinhacao()



