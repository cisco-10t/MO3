original="abcdefghijklmnopqrstuvwxyz "
codigo="bcdefghijklmnopqrstuvwxyza "

def menu():
    opçao=input("Quer (c)codificar ou (d)descodificar uma mensagem?: ")
    if opçao.lower()=="c":
        codificar()
    elif opçao.lower()=="d":
        descodificar()

def codificar(mensagem):
    global original
    global codigo
    codificado=""
    mensagem=mensagem.lower()
    for l in mensagem:
        for p in range(len(original)):
            if l==original[p]:
                codificado+=codigo[p]
    return codificado

def descodificar(mensagem):
    global original
    global codigo
    descodificado=""
    mensagem=mensagem.lower()
    for l in mensagem:
        for p in range(len(original)):
            if l==original[p]:
                descodificado+=codigo[p]
    return descodificado