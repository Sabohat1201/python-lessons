#*args-arguments
# def summa(*sonlar):
#   """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi=0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# print(summa(1,2,3))
# print(summa(4,5,6,7))
#2 - usul.
# def summa(*sonlar):
#   """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)
# print(summa(8,9))

# def summa(x,y,*sonlar):
#   """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)
# print(summa(3,4,5))

#**kwargs - keywords arguments - kalit so'zli argumentlar
# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqida ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto1=avto_info('GM','malibu',rangi='qora',yili=2018)
# avto2=avto_info('Kia','K5',rang='qizil',yili=2020,narhi=35000)
# print(avto1)
# print(avto2)

#AMALYOT
#1 - SHART.Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
# def multiplication(*sonlar):
#     """Kiritilgan sonlar yig'indisini qabul qiluvchi funksiya"""
#     kopaytma=1
#     for son in sonlar:
#         kopaytma*=son
#     return kopaytma
# print(multiplication(5,6,8))

#2 - SHART.Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. 
# Talabaning ismi va familiyasi majburiy argument, 
# qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
def students(ism,familiya,**malumotlar):
    """Talabalar haqidagi ma'lumotlarni lug'at ko'rinshida qaytaruvchi funksiya"""
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar
talaba1=students('Sabohat','Qayumova',yoshi=24,kurs=4,fakultet='telekomunikatsiyalar')
talaba2=students('Madina','Bobomurodova',yoshi=25,kurs=4)
talabalar=[talaba1,talaba2]
print(talabalar)