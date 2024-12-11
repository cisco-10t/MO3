import math
#calcula a exponenciaçao utilizando o operador
from datetime import datetime
import time
def funcao_complicada():
    for i in range(1000000):
        _=i**2

#calcula a exponenciaçao utilizando a funcao pow do modulo math
def funcao_complicada2():
    for i in range(1000000):
        _=math.pow(i,2)

def medir_tempo():
    inicio=datetime.now()
    funcao_complicada()
    fim=datetime.now()
    tempo_execuçao=fim-inicio
    print("tempo de execuçao:", tempo_execuçao.total_seconds())

medir_tempo()