import random as rand

def line():
    print("-=" * 16)

def jogar():
    line()
    print("Jogo da forca")
    line()

    with open("words.txt", "r") as file:
        words = [x.strip() for x in file]



    enforcou = False
    acertou = False

    secret = words[rand.randrange(0,len(words) + 1)].upper()
    palavra = ["_" for letra in secret]
    erros = 0

    while (not enforcou and not acertou):
        chute = input("Qual a letra? ").strip().upper()
        indice = 0
        if chute in secret:
            for letra in secret :
                if(chute == letra):
                    palavra[indice] = chute
                indice += 1
        
        else:

            erros += 1
            print(f"Voce errou! Ainda faltam {6 - erros} tentativas.")

        print(palavra)
        enforcou = erros == 6
        acertou = ("_" not in palavra)

        if(acertou):
            line()
            print("Você ganhou")
        
        if(enforcou):
            line()
            print(f"Você perdeu\nA palavra era {secret}")

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()