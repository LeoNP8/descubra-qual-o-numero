import random
def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 5
    while tentativas < max_tentativas:
        palpite = int(input("Tente adivinhar o número: "))
        if palpite == numero_secreto:
            print(" Parabéns você acertou!")
            break
        elif palpite > numero_secreto:
            print("Tente um numero menor.")
        else:
            print("Tente um número maior.")
            tentativas += 1
    if tentativas == max_tentativas:
        print(f"Fim de jogo. O número era {numero_secreto}." )
# Chamando a função para iniciar o jogo
jogo_adivinhacao()