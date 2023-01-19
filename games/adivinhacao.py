import random as rand

def line():
    print("-=" * 16)

def choice_num():

    while True:
        num = int(input("Aleatorizar um numero entre 1 e : "))
        if (num >= 10):
            break
        else:
            print("escolha um numero maior ou igual a 10")
            line()
    return num

def jogar():
    line()
    print("Jogo de adivinhacao")
    line()

    secret = rand.randrange(1, choice_num() + 1)

    while True:
        line()
        choice = verify_num()
        if(choice > secret):
            print("O numero sorteado é menor do que o escolhido")
        elif(choice < secret):
            print("O numero sorteado é maior do que o escolhido")
        else:
            print("Parabens! Você acertou o numero")
            break

if (__name__ == "__main__"):
    jogar()

def verify_num():
    while True:
        choice = input("Tente adivinhar o numero: ")
        if(choice in range(0,10)):
            return int(choice)