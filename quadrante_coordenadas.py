

import utils
def quadrantes():
    x=utils.ler_nº_decimal("Introduza as coordenadas de X do ponto P: ")
    y=utils.ler_nº_decimal("Introduza as coordenadas de Y do ponto P: ")
    if x==0 or y==0:
        return f"As coordenadas de P({x},{y}) se encontram nos eixos."
    elif x>0 and y>0:
        return f"As coordenadas de P({x},{y}) se encontra no 1º quadrante."
    elif x<0 and y>0:
        return f"As coordenadas de P({x},{y}) se encontra no 2º quadrante."
    elif x<0 and y<0:
        return f"As coordenadas de P({x},{y}) se encontra no 3º quadrante."
    elif x>0 and y<0:
        return f"As coordenadas de P({x},{y}) se encontra no 4º quadrante."

"""
FEITO POR XICUUMUEDAS
x=float(input("Introduza as coordenadas de X do ponto P: "))
y=float(input("Introduza as coordenadas de Y do ponto P: "))
if x>0 and y>0:
    print("As coordenadas pertencem ao 1º quadrante.")
elif x<0 and y>0:
    print("As coordenadas pertencem ao 2º quadrante.")
elif x<0 and y<0:
    print("As coordenadas pertencem ao 3º quadrante.")
elif x>0 and y<0:
    print("As coordenadas pertencem ao 4º quadrante.")
elif x==0 or y==0:
    print("As coordenadas estão sobre os eixos.")
"""

def main():
    
    print(quadrantes())
if __name__=="__main__":
    main()