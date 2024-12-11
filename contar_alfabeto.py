def contar_alfabeto(alfabeto,palavra):
    for letra in alfabeto:
        contar=0
        for letra2 in palavra:
            if letra==letra2:
                contar+=1
        print(contar)


def menu():
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    palavra=input("que frase quer contar meu nobre??: ")
    contar_alfabeto(alfabeto,palavra)
def main():
    menu()
if __name__=="__main__":
    main()