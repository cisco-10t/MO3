
def contar_alfabeto(palavra):
    for i in range(97,123):
        contar=0
        for letra in palavra:
            if i==ord(letra):
                contar+=1
        print(contar)

def menu():
    
    palavra=input("que frase quer contar meu nobre??: ")
    contar_alfabeto(palavra)

def main():
    menu()
if __name__=="__main__":
    main()