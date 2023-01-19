import adivinhacao
import forca
import os

def line():
    print("-=" * 16)


def verify_num():
    error=""
    while True:
        os.system("clear")
        print(error)
        print("Qual jogo você deseja jogar?")
        try:
            choice = int(input("(1)Adivinhação\n(2)Forca\n(3)Sair\nEscolha: "))
            if(choice in range(1,4)):
                return int(choice)
            else:

                error="Escolha entre 1 e 2!"
        except:
            error="Escolha apenas numeros!"

line()
choice = verify_num()
line()

if(choice == 1):
    adivinhacao.jogar()
elif(choice == 2):
    forca.jogar()
elif(choice == 3):
    exit()