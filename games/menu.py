import adivinhacao

def line():
    print("-=" * 16)

line()
print("Qual jogo você deseja jogar?")
choice = int(input("(1)Adivinhação\n(2)Forca\nEscolha: "))
line()
if(choice == 1):
    adivinhacao.jogar()
elif(choice == 2):
    forca.jogar()