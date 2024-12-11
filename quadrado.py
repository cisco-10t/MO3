import math
def quadrado(x):
    quadrado=math.pow(x,2)
    return quadrado
def main():
    x=int(input("Insira um nº: "))
    print(quadrado(x))
if __name__=="__main__":
    main()