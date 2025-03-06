import datetime as dt
#datetime
hozir=dt.datetime.now()
print(hozir)
#Sanani ajratib olish
print(hozir.date())
#Vaqtni ajratib olish
print(hozir.time())
#Soatni ajratib olish
print(hozir.hour)
#Minutni ajratib olish
print(hozir.minute)
#Sekundni ajratib olish
print(hozir.second)

#data()
bugun=dt.date.today()
print(F"Bugun sana: {bugun}")
ertaga=dt.date(2025,3,7)
print(f"Ertaga sana: {ertaga}")

#time()
hozir=dt.datetime.now()
vaqtHozir=hozir.time()
print(vaqtHozir)
vaqtKeyin=dt.time(23,59,00)
print(vaqtKeyin)

#Sanalar orasidagi farq 
bugun=dt.date.today()
ramazon=dt.date(2025,3,30)
farq=ramazon-bugun
print(farq)
print(f"Ramazon tugashiga {farq.days} kun qoldi!")

#Soatlar orasidagi farq
hozir=dt.datetime.now()
navroz=dt.datetime(2025,3,21,1,30,0)
farq=navroz-hozir
print(farq)
sekundlar=farq.seconds
minutlar=int(sekundlar/60)
soatlar=int(minutlar/60)
print(f"Navro'z kelishiga {farq.days} kun {soatlar} soat qoldi!")

#math moduli
import math 
PI=math.pi
print(f"PI ning qiymati: {PI}")
e=math.e
print(f"e ning qiymati: {e}")

#trigonametriya
print(math.sin(math.pi/2))
print(math.cos(0))
print(math.tan(PI))
#radianlar va burchaklar o'rtasidagi konvertatsiya
print(math.degrees(math.pi/2))
print(math.radians(90))
#logorifmlar
#natural logarifm
print(math.log(5))
#10 asosli logarifm
print(math.log10(100))

#Sonlarni yaxlitlash
x=4.6
print(math.ceil(x))
print(math.floor(x))
print(round(4.6))

#Kvadrat ildiz
x=81
print(math.sqrt(x))

#Darajaga oshirish
print(math.pow(x,3))# x ning kubi
print(math.pow(x,5))# x ning 5 chi darajasi
print(math.pow(x,1/3))# x dan kub ildiz

# pprint moduli
from pprint import pprint
import json
filename="data/bemor.json"
with open(filename) as f:
    bemor=json.load(f)
print(bemor)
pprint(bemor)

# RegEx - Regular Expressions
import re
from uzwords import words
word1="темир"
word2="томир"
word3="тулпор"
andoza="^т...р$"
print(re.match(andoza,word1))
print(re.match(andoza,word2))
print(re.match(andoza,word3))

matches=[]
for word in words:
    if re.match(andoza,word):
        matches.append(word)
print(matches)

#Emailni ajratib olish
matn ="""Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """
andoza="[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
print(re.findall(andoza,matn))

#Kuchli parolni tekshirish
andoza='^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg="Yangi parol kiriting"
msg+="(kamida 8 ta belgidan iborat,kamida 1 ta lotin bosh harf,1 ta kichik harf,"
msg+="1 ta son va 1 ta maxsus belgi bo'lishi kerak.)"
while True:
    password=input(msg)
    if re.match(andoza,password):
        print("Maxfiy so'z qabul qilindi.")
        break
    else:
        print("Maxfiy so'z talabga javob bermaydi.")