def Media():
    n1=int(input("insira um nº: "))
    n2=int(input("insira um nº: "))
    n3=int(input("insira um nº: "))
    n4=int(input("insira um nº: "))
    n5=int(input("insira um nº: "))
    soma=n1 + n2 + n3 + n4 + n5
    media=soma/5
    print(media)


def Media2():
    soma=0
    for _ in range(5):
        n=int(input("insira um nº: "))
        soma=soma+n
    media=soma/5
    print(media)

