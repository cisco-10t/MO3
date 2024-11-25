def palindromo(palavra) ->bool:
    palavra_invertida=""
    palindromo=False
    for i in range(len(palavra)-1, -1, -1):
        palavra_invertida = palavra_invertida + palavra[i]
    if palavra_invertida == palavra:
        palindromo=True
    return palindromo
def main():
    palavra=input("insira uma palavra: ")
    print(palindromo(palavra))
    P=palindromo(palavra)
    if P==True:
        print(f"A palavra {palavra} é um palindromo")
    else:
        print(f"A palavra {palavra} nao é um palindromo")
if __name__=="__main__":
    main()