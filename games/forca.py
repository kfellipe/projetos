def line():
    print("-=" * 16)

def jogar():
    line()
    print("Jogo da forca")
    line()

    enforcou = False
    acertou = False

    secret = "olimpiadas"

    while (not enforcou and not acertou):
        chute = input("Qual a letra? ").strip()
        indice = 0
        for letra in secret :
            if(chute.upper() == letra.upper()):
                print(f"Foi encontrado a letra {chute} na posição {indice}")
            indice += 1


if(__name__ == "__main__"):
    jogar()