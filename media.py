def mediaA():
    n1=int(input("Insira um numero: "))
    n2=int(input("Insira outro numero: "))
    n3=int(input("Insira outro numero: "))
    print("A média dos 3 numeros é", (n1+n2+n3)/3)

def mediaB(n1,n2,n3):
    media=(n1+n2+n3)/3
    print("A média é {media}")

def mediaC():
    n1=int(input("Insira um numero: "))
    n2=int(input("Insira outro numero: "))
    n3=int(input("Insira outro numero: "))
    media=(n1+n2+n3)/3
    return media

def mediaD(n1,n2,n3):
    media=(n1+n2+n3)/3
    return media


def main():
    mediaA()
    n1=int(input("Insira um nº: "))
    mediaB(5,5,5)
    print(f" A média é {mediaC()}")
    print(f"A média é {mediaD(5,5,5)}")

if __name__=="__main__":
    main()

