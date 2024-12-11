import utils
def entradacliente(mcliente,acliente,mmesa,amesas):
    if mmesa==amesas:
        print(f"Não pode entrar mais clientes, todas as mesas estao ocupadas ⚠️.")
    elif acliente==mcliente:
        print("O restaurante esta cheio ⚠️")
        return 0
    else:
        livres=mcliente-acliente
        centrada=utils.ler_nº_inteiro_limites(1,livres,"Quantos clientes entraram?: ")
        return centrada
    return 0

def entradamesas(mmesa,amesas,mclientes,aclientes):
    if mclientes==aclientes:
        print("O restaurante ja está com a capacidade maxima de clientes, não se pode ocupar mesas ⚠️.")
    elif amesas==mmesa:
        print("As mesas estam todas ocupadas ⚠️")
    else:
        livres=mmesa-amesas
        mocupadas=utils.ler_nº_inteiro_limites(1,livres,"Quantas mesas foram ocupadas?: ")
        return mocupadas
    return 0

def saidaclientes(aclientes):
    if aclientes==0:
        print("O restaurante esta vazio ⚠️.")
        return 0
    sairam=utils.ler_nº_inteiro_limites(1,aclientes,"Quantos clientes sairam?: ")
    return sairam

def saidamesas(amesas):
    if amesas==0:
        print("As mesas estao todas vazias ⚠️.")
        return 0
    sairam=utils.ler_nº_inteiro_limites(1,amesas,"Quantos mesas foram desocupadas?: ")
    return sairam

def saidacusto(saidacl,acliente):
    if acliente>0:
        precot=0
        for i in range(1,saidacl+1):
            preco=utils.ler_nº_decimal_limites(0,None,f"Quanto pagou o  {i}º cliente a sair do restaurante?: ")
            precot+=preco
        return precot
    return 0

def estado(atclientes,atmesas,maxclientes,maxmesas,totalganho):
    mesaslivres=maxmesas-atmesas
    pclientes=atclientes/maxclientes*100
    print(f"O restaurante tem {atmesas} mesas ocupadas e {mesaslivres} livres\nTem {atclientes} clientes no restaurante com  {pclientes}% de sua capacidade maxima\nE o lucro do restaurante até agora são {totalganho}€.")

def menu():
    maxclientes=utils.ler_nº_inteiro("Quantos clientes o restaurante pode receber?: ")
    maxmesas=utils.ler_nº_inteiro("Quantas mesas o restaurante tem?: ")
    atmesas=0
    atclientes=0
    totalganho=0
    op=22
    while op!=4:
        op=utils.ler_nº_inteiro_limites(1,4,"1.Entrada\n2.Saída\n3.Estado\n4.Terminar\n: ")
        if op==1:
            entraram_clientes=entradacliente(maxclientes,atclientes,maxmesas,atmesas)
            atclientes+=entraram_clientes
            mesas_ocupadas=entradamesas(maxmesas,atmesas,maxclientes,atclientes)
            atmesas+=mesas_ocupadas
        elif op==2:
            saidac=saidaclientes(atclientes)
            atclientes-=saidac
            saidam=saidamesas(atmesas)
            atmesas-=saidam
            preco=saidacusto(saidac,atclientes)
            totalganho+=preco
        elif op==3:
            estado(atclientes,atmesas,maxclientes,maxmesas,totalganho)
            
def main():
    menu()

if __name__=="__main__":
    main()