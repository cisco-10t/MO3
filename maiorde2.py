def maiorde2(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    return None
def main():
    a=float(input("Insira um numero: "))
    b=float(input("Insira um numero: "))
    print(maiorde2(a,b))
if __name__=="__main__":
    main()