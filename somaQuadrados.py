import quadrado
def soma_quadrados(x):
    soma=0
    for i in range(1,x+1):
        soma=soma+quadrado.quadrado(i)
    return int(soma)
def main():
    x=int(input("Insira um nº: "))
    print(soma_quadrados(x))
if __name__=="__main__":
    main()
