#lambda - nomsiz vaqtinchalik funksiya
import math 
uzunlik = lambda pi,r: 2*pi*r
print(uzunlik(math.pi,10))

kvadrat=lambda x,y:x**y
print(kvadrat(3,2))

def daraja(n):#Funksiya yasaydigan funksiya
    return lambda x:x**n
kvadrat=daraja(2)
kub=daraja(3)
print(f"3 - ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng.")

from math import sqrt
sonlar=list(range(11))
ildizlar=list(map(sqrt,sonlar))#map-bitta funksiya va bitta ro'yhat qaytaradi
print(ildizlar)

def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x
print(list(map(daraja2,sonlar)))
#1 - usul
kvadratlar=list(map(lambda x: x*x,sonlar))
print(kvadratlar)
#2 - usul
kvadratlar=[]
for son in sonlar:
    kvadratlar.append(son*son)
print(kvadratlar)

a = [4,5,6]
b = [7,8,9]
a_plus_b=list(map(lambda a,b:a+b,a,b))
print(a_plus_b)

import random as r
sonlar=r.sample(range(100),10)
print(sonlar)
def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchi funksiya"""
    return x%2==0
#1 - usul
juft_sonlar=list(filter(juftmi,sonlar))
print(juft_sonlar)
#2-usul
juft_sonlar2=list(filter(lambda son:son%2==0,sonlar))
print(juft_sonlar2)

mevalar=['olma','anor','anjir','shaftoli','o\'rik','tarvuz','qovun','banan']
harf='b'
mevalar_b=list(filter(lambda meva:meva.startswith(harf),mevalar))
print(mevalar_b)

mevalar2=list(filter(lambda meva:len(meva)<=5,mevalar))
print(mevalar2)

mevalar3=list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')),mevalar))
print(mevalar3)

#AMALYOT
def tubmi(x):
    if x % 2 == 0 or x < 2:
        return False  # Son juft yoki 2 dan kichik bo'lsa
    if x == 2 or x == 3:
        return True  # Son 2 yoki 3 bo'lsa
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True


tub_sonlar = list(filter(tubmi, range(100)))
print(tub_sonlar)