import datetime
def estacionamento(horas:int,minutos:int)->int:
    hora_atual=datetime.datetime.now().hour
    minutos_atuais=datetime.datetime.now().minute
    n_horas=hora_atual-horas
    n_minutos=minutos_atuais-minutos
    if n_minutos<0:
        n_horas-=1
        n_minutos=60-minutos+minutos_atuais
    duracao_total_minutos=n_horas*60+n_minutos
    return duracao_total_minutos
def blocosminutos(minutos:int)->int:
    n_blocos=minutos//15
    if minutos%15!=0:
        n_blocos+=1
    return n_blocos
def custo(blocos:int,preço:float)->float:
    return blocos*preço
def main():
    preço=float(input("Quanto fica o estacionamento por 15min?: "))
    horas=int(input("A que horas o carro chegou?: "))
    minutos=int(input("A que minutos o carro chegou?: "))
    duracao_minutos=estacionamento(horas,minutos)
    blocos=blocosminutos(duracao_minutos)
    Custo=custo(blocos,preço)
    print(f"Estacionamento com duraçao de {duracao_minutos} que corresponde a {blocos} de 15 minutos com o custo de {custo}€")
if __name__=="__main__":
    main()