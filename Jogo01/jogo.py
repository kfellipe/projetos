import random
def lin():
    print("=" * 40)

def erro():
    print("[ERROR]Digite Apenas NÚMEROS!")
    lin()

while True:
    escuser1 = input("Escolha um número: ")
    lin()
    if escuser1.isnumeric():
        escuser = int(escuser1)
        escom = random.randint(0, escuser)
        tent = 0
        while True:
            tryuser1 = input(f"tente acertar o número de 0 a {escuser}: ")
            tent += 1
            if tryuser1.isnumeric():
                tryuser = int(tryuser1)
                if tryuser < escom:
                    print("Mais!!!")
                    lin()
                if tryuser > escom:
                    print("Menos!!!")
                    lin()
                if tryuser == escom:
                    print(f"PARABÈNS!!! \nVocê acertou o número! \nVocê ACERTOU em {tent} tentativas!!!")
                    lin()
                    print(f"Deseja jogar novamente? \n1 - Tentar Novamente \n2 - Sair")
                    while True:
                        esctent1 = input("Escolha: ")
                        if esctent1.isnumeric():
                            esctent = int(esctent1)
                            if esctent == 1:
                                lin()
                                break
                            if esctent == 2:
                                print("Obrigado por Jogar!")
                                exit(0)
                            else:
                                print("[ERROR]Digite 1 ou 2!")
                                lin()
                        else:
                            erro()
                    break
            else:
                erro()
    else:
        erro()