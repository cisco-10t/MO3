
def somar(a,b):
    print(a+b)
    a=0
    b=0

def main():
    somar("Joaquim","Maria")
    somar(10,5)
    somar(10.3,-3.2)
    n=10
    z=15
    somar(n,z)
    print(n,z)

if __name__=="__main__":
    main()