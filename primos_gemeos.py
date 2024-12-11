"""
dois nº primos gemeos sao dois nº primos q distam em 2 unidades um do outro
p.ex:
    3 e 5
    5 e 7
fazer um programa q lê dois nº inteiros positivos do utilizador e diz se sao primos e primos gemeos
"""
import primo
from utils import ler_nº_inteiro
n1=utils.ler_nº_inteiro("insira um nº: ")
n2=utils.ler_nº_inteiro("insira um nº: ")
if primo.Primo(n1) and primo.Primo(n2):
    diferença=n1-n2
    if abs(diferença)==2:
        print(f"os valores {n1} e {n2} sao primos gemeos")
    else:
        print(f"os valores {n1} e {n2} sao primos")
else:
    if primo.Primo(n1):
        print(f"o valor {n1} é primo")
    elif primo.Primo(n2):
        print(f"o valor {n2} é primo")
    else:
        print("nenhum dos valores é primo")