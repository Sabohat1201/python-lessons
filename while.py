#input() - funksiyasi
# ism=input("Ismingiz nima? ")
# yosh=int(input(f"Salom {ism.title()}. Yoshingiz nechida?"))
# height=float(input("Bo'yingiz nechida? "))
# print(yosh)
# print(height)

#while() - funksiyasi
# son=1
# while son<=5:
#     print(f"{son} ning kvadrati {son**2} ga teng.")
#     son += 1

#while() and input() funksiyasi
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol="Istalgan sonni kiriting: "
savol+="(dasturni to'xtatish uchun 'exit' ni bosing.):"
# qiymat=''
# while qiymat!='exit':
#     qiymat=input(savol)
#     if qiymat!='exit':
#         print(float(qiymat)**2)
#     else:
#         print("Dastur tugadi.")

#ishora(flag)
# ishora=True
# while ishora:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         ishora=False
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi")

#BREAK operatori
# while True:#abadiy sikl
#     qiymat=input(savol)
#     if qiymat == 'exit':
#         break#tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)

#for siklini to'xtatish uchun ham break operatiri qo'llaniladi
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son==5:
#         break
#     else:
#         print(f"{son} ning kvadrati {son**2} ga teng.")

#CONTINUE   break operatorini teskarisi
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son==5:
#         continue
#     else:
#         print(f"{son} ning kvadrati {son**2} ga teng.")

son=0
while son<10:
    son+=1
    if son%2!=0:
        continue
    else:
        print(son)
