
"""
for i in range(10):
    print(i)
    i=0
"""

def funcaoA():
    x=0
    while x<10:
        x+=1
        return x
"""
print(funcaoA())
print(funcaoA())
print(funcaoA())
"""

def funcaoB():
    x=0
    while x<100000000000:
        x+=1
        yield x

for i in funcaoB():
    print(i)
    i=0
