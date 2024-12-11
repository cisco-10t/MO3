def ler_nº_inteiro(mensagem)->int:
    """
    funçao q le do utilizador u nº inteiro. A funçao garante q o valor inserido é um valor valido
    """
    while True:
        dados=input(mensagem)
        if len(dados)==0:
            continue
        #verificar se existe um - no inicio da str(valor negativo)
        if dados[0]=="-":
            testar=dados.replace("-"," ")
        else:
            testar=dados

        if testar.isdigit():
            return int(dados)
        print("o valor inserido nao é valido.")

def ler_nº_inteiro_limites(valor_min,valor_max=None, mensagem="introduza valor inteiro: ")->int:
    """
    funçao q recebe o valor min e max a ler do utilizador. A funçao devolve o valor quando é um inteiro valido
    """
    while True:
        numero=ler_nº_inteiro(mensagem)
        if numero>=valor_min and (valor_max is None or numero<=valor_max):
            return numero
        print("Erro: O valor nao é valido.")

def ler_nº_decimal(mensagem="introduza um valor decimal: ") -> float:
    """  
    funçao pra ler um nº decimal. A funçao garante q o valor é valido e aceita como separador das casas decimais . ou ,
    """  
    while True:
        dados=input(mensagem)
        if len(dados)==0:
            continue
        #substituir as virgulas por pontos
        dados=dados.replace(',','.')
        #verificar se existe um - no inicio da str(valor negativo)
        if dados[0]=="-":
            testar=dados.replace("-","")
        else:
            testar=dados
        #contar os pontos decimais
        pontos=testar.count('.')
        #remover os pontos decimais
        testar=testar.replace('.','')
        #n pode ter mais de um ponto decimal e so pode ter digitos

        if testar.isdigit() and pontos<=1:
            return float(dados)
        print("o valor inserido nao é valido.")

def ler_nº_decimal_limites(valor_min,valor_max=None,mensagem="introduza um valor: ")->float:
    while True:
        valor=ler_nº_decimal(mensagem)
        if valor>=valor_min and (valor_max is None or valor<=valor_max):
            return valor
        print("Erro: valor nao é valido")