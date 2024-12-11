def n_mm(x,y,z):
    maior=x
    menor=x
    if y>maior:
        maior=y
    elif y<menor:
        menor=y
    if z>maior:
        maior=z
    elif z<menor:
        menor=z
    if x>=0 and y>=0 and z>=0:
        return maior
    elif x<0 and y<0 and z<0:
        return menor