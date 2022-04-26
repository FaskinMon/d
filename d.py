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

def bag(a):
    d=random.randint(1,5)
    print(d)
    if d==a:
        return
    bag(a)
    



bag(1)
    
