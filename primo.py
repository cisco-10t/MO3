def primo(n)-> bool:
    E_primo=True
    for i in range(2,n):
        if n%i==0:
            E_primo=False
            break
    return E_primo
def main():
    n=int(input("Insira um numero: "))
    print(f"")

if __name__=="__main__":
    main()