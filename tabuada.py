def tabuada(n):
    for i in range(1,11):
        print(f"{n} x {i}= {n*i}")
def main():
    x=int(input("Tabuada do: "))
    tabuada(x)
if __name__=="__main__":
    main()