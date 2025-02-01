#Ro'yhat
# print("Yaqin do'stlaringizni ro'yhatini tuzamiz.")
# ismlar=[]
# n=1
# while True:
#     savol=f"{n} - do'stingizni ismini kiriting: "
#     ism=input(savol)
#     ismlar.append(ism)
#     takrorlash= input("Yana ism qo'shasizmi? (ha/yo'q)")
    
#     if takrorlash == 'ha':
#         n+=1
#         continue
#     else:
#         break
# print("Do'stlaringiz ro'yhati: ")
# for ism in ismlar:
#     print(f"{ism.title()}")

#Lug'at
# print("Do'stlaringizni yoshini tuzamiz: ")
# dostlar={}
# ishora=True
# while ishora:
#     ism=input("Do'stingizni ismini kiriting: ")
#     yosh=input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism]=int(yosh)
#     savol=input("Yana do'stingizni qo'shasizmi? (ha/yo'q)>>>")
#     if savol=='yo\'q':
#         ishora=False
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

#remove() funksiyasi
# cars=['lasetti','nexia','toyota','nexia','audi','malibu','nexia','lasetti']
# car='lasetti'
# while car in cars:
#     cars.remove(car)
# print(cars)

talabalar=['hasan','husan','olim','botir']
baholangan_talabalar={}
while talabalar:#toki talabalar ro'hatida element bor ekan tsikl takrorlansin
    talaba=talabalar.pop()
    baho=input(f"{talaba.title()}ning bahosini kiriting: ")
    baholangan_talabalar[talaba]=int(baho)

print(baholangan_talabalar)