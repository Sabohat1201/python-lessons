#Jumboq 1 dan 100 gacha bo'lgan sonlar ro'yhatidan qolib ketgan sonni topish
#1 - usul
import random as r
n = 100
numbers=list(range(1,n+1))
x= numbers.pop(r.randint(1,n+1))
#print(x)
numbers2=list(range(1,n+1))
#print(sum(numbers2)-sum(numbers))

#2 - usul
for i in range(1,n):
    if i not in numbers:
        print(i)
        break

#3 - usul 
summa=n*(n+1)//2
print(summa-sum(numbers))