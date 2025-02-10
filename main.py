#1 - USUL
# import avto_info_mod 
# avto1=avto_info_mod.avto_info('GM','Malibu','Qora','avtomat',2020,40000)
# avto_info_mod.info_print(avto1)

#2 - USUL
# import avto_info_mod as aim
# avto1 = aim.avto_info('GM','Malibu','Qora','avtomat',2020,40000)
# aim.info_print(avto1)

#3 - USUL
# from avto_info_mod import avto_info,info_print
# avto1=avto_info('GM','Malibu','Qora','avtomat',2020,40000)
# info_print(avto1)

#4 - USUL
# from avto_info_mod import avto_info as ainfo, info_print as iprint
# avto1=ainfo('GM','Malibu','Qora','avtomat',2020,40000)
# iprint(avto1)

#5 - USUL tavsiya etilmaydi
# from avto_info_mod import *
# avto1=avto_info('GM','Malibu','Qora','avtomat',2020,40000)
# info_print(avto1)

# import math
# x=400
# print(math.sqrt(x))
# print(math.pow(5,3))#darajani hisoblaydi.
# print(math.pi)
# print(math.log2(8))
# print(math.log10(100))

import random as r
#randint - random usulida son tanlab oladi
son=r.randint(0,100)
print(son)

#choice - ro'yhat ichidan bittasini tanlab oladi.
ismlar=['sabohat','madina','olim','murod','nilufar']
ism=r.choice(ismlar)
print(ism)

x=list(range(0,51,5))
print(x)
print(r.choice(x))

#shuffle - aralashtirib tashlaydi
y=list(range(11))
print(y)
r.shuffle(y)#bunda o'zgaruvchiga yuklab bo'lmaydi.
print(y)