import math
def hipotenusa(a1,a2):
    hipotenusa=a1**2+a2**2
    hipotenusa=math.sqrt(hipotenusa)
    return round (hipotenusa,3)
def main():
    a1=int(input("Insira um cateto do triangulo: "))
    a2=int(input("Insira outro cateto de triangulo: "))
    print(hipotenusa(a1,a2))
if __name__=="__main__":
    main()
