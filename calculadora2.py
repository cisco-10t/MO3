def somar():
    a=float(input("insira um numero: "))
    b=float(input("insira um numero: "))
    print("a soma dos dois numeros é", a+b)
def subtrair():
    a=float(input("insira um numero: "))
    b=float(input("insira um numero: "))
    print("a subtraçao dos dois numeros é", a-b)
def multiplicar():
    a=float(input("insira um numero: "))
    b=float(input("insira um numero: "))
    print("a multiplicaçao dos dois numeros é", a*b)
def dividir():
    a=float(input("insira um numero: "))
    b=float(input("insira um numero: "))
    print("a divisao dos dois numeros é", a/b)
def menu():
    op="0"
    while op!="5":
        print("1.somar\n2.subtrair\n3.multiplicar\n4.dividir\n5.terminar")
        op=input()
        if op=="1":
            somar()
        elif op=="2":
            subtrair()
        elif op=="3":
            multiplicar()
        elif op=="4":
            dividir()
def main():
    menu()
if __name__=="__main__":
    main()