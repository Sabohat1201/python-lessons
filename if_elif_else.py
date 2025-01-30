# yosh=int(input("Yoshingiz nechida? "))
# if yosh<=4:
#     print("Sizga kirish bepul!")
# elif yosh<12:
#     print("Sizga kirish 5000 so\'m!")
# elif yosh<=18:
#     print("Sizga kirish 8000 so\'m!")
# else:
#     print("Sizga kirish 10000 so\'m")
# yosh=int(input("Yoshingiz nechida? "))
# if yosh<=4:
#     narh=0
# elif yosh<12:
#     narh=5000
# elif yosh<=18:
#     narh=8000
# else:
#     narh=10000
# print(f"Sizga kirish {narh} so\'m")
# kun=input("Bugun nima kun? ")
# if kun.lower() == 'yakshanba' or kun.lower() == 'shanba':
#     print("Bugun dam olish kuni!")
# else:
#     print("Bugun ish kuni!")
# kun=input("Bugun kun nima? ")
# harorat=int(input("Havo harorati qanday? "))
# if kun.lower() == 'yakshanba' or kun.lower() == 'shanba' and harorat>30:
#     print("Cho'milgani ketdik!")
# elif kun.lower() == 'yakshanba' or kun.lower() == 'shanba'and harorat<30:
#     print("Bugun uyda dam olamiz!")
# else:
#     print("Bugun ish kuni!")
# narh=15000
# choy=True
# salat=False
# if choy and salat:
#     narh=narh+10000
# elif salat or choy:
#     narh=narh+5000
# print(f"Jami {narh} so\'m bo'ldi!")
# narh=15000
# choy=1
# salat=0
# non=1
# kompot=1
# assorti=0
# if choy:
#     print("Mijoz choy oldi.")
#     narh=narh+5000
# if salat:
#     print("Mijoz salat oldi.")
#     narh=narh+10000
# if non:
#     print("Mijoz non oldi.")
#     narh=narh+5000
# if kompot:
#     print("Mijoz kompot oldi")
#     narh=narh+8000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narh=narh+15000
# print(f"Jami {narh} so\'m bo\'ldi.")

#menu=['osh','shashlik','manti','somsa','norin','qozonkabob']
#buyurmalar=['shashlik','lag\'mon','manti','sh\'rva']
# ovqat = input("Nima ovqat yeysiz? ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi!")
# else:
#     print("Afsuski menuda bunday taom yo\'q!")

# menu=['osh','shashlik','manti','somsa','norin','qozonkabob']
# buyurtmalar=['shashlik','lag\'mon','manti','sh\'rva']
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor!")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q!")
# else:
#     print("Savatchangiz bo\'sh!")


#AMALYOT
# j_son=float(input("Juft son kiriting: "))
# if j_son%2:
#     print("Bu juft son emas.")
# else:
#     print("Rahmat!")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinnchi sonni kiriting: "))
# if x>y:
#     print(f"{x}>{y}")
# elif x<y:
#     print(f"{x}<{y}")
# elif x == y:
#     print(f"{x}={y}")

# d_mevalar=['uzum','olma','qulupnay','banan','gilos']
# savat=[]
# for n in range(0,5):
#     savat.append(input(f"Savatingizga {n+1} mahsulotni kiriting: "))
# if savat:
#     for mahsulot in savat:
#         if mahsulot in d_mevalar:
#             print(f"Do'konimizda {mahsulot} bor.")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q.")
# else:
#     print("Savatingiz bo'sh.")

# mahsulotlar=['gilos','tarvuz','olcha','mandarin']
# savat=[]
# for n in range(0,5):
#     savat.append(input(f"Savatingizga {n+1} - mahsulotni qo'shing: "))
# if savat:
#     print("Do\'konimizda quyidagi mahsulotlar yo\'q:")
#     for mahsulot in savat:
#         if mahsulot not in mahsulotlar:
#             print(f"{mahsulot}")

# users=['Murod','Guli',"Madina"]
# login=input("Yangi login tanlang: ")

# if login.title() not in  users:
#     print("Xush kelibsiz!")
# else:
#     print("Login band, yangi login tanlang!")

# son = int(input("Istalgan butun sonni kiriting: "))
# for n in range(2,11):
#     if not son % n:
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

