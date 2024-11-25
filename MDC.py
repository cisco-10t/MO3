def MDC(a,b):
    menor=a
    if b<menor:
        menor=b
    maior_divisor=None 
    for i in range(2,menor):
        if a%i==0 and b%i==0:
            maior_divisor=i
    return maior_divisor

assert MDC(5,10)==None
assert MDC(6,12)==3
assert MDC(12,6)==3
assert MDC(12,18)==6
assert MDC(10,20)==5