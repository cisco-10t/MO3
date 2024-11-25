def Soma(x,y):
    t=x+y
    return t
x=Soma(10,5)
print(x)
print(Soma(5,10))
x=int(input("X: "))
y=int(input("Y: "))
z=int(input("Z: "))
print(Soma(x,Soma(y,z)))