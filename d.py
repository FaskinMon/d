import random
#Рефлексия
run=True
while run:
    d=random.randint(1,5)
    print(d)
    if d==1:
        break
print('------------')
#Рекрусия

def bаg(a):
    d=random.randint(1,5)
    print(d)
    if d==a:
        return
    bag(a)
    



bag(1)
    
