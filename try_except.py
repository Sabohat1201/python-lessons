#ValueError
#yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh=int(yosh)
# except ValueError:
#     print("Siz butun son kiritmadingiz.")
# else:
#     print(f"Siz {2025-yosh} yilda tug'ilgansiz.")

#ZeroDivisionError
x,y=5,10
try:
    y/(x-5)
except ZeroDivisionError:
    print("0 ga bo'lish mumkin emas.")

#IndexError
mevalar=['olma','anor','anjir','uzum']
try:
    print(mevalar[4])
except:
    print(f"Ro'yhatda {len(mevalar)} ta meva bor xolos.")

#KeyError
user={
    "username":"Sabohat",
    "status":"admin",
    "email":"saboxatqayumova7@gmail.com",
    "phone":"998977777777"
}
key="email"
try:
    print(f"Foydalanuvchi: {user[key]}")
except KeyError:
    print("Bunday kalit mavjud emas.")

#FileNotFoundError
filename='data.txt'
try:
    with open(filename) as file:
        text=file.read()
except FileNotFoundError:
    print(f"{filename} mavjud emas.")

import json
files=['data/talaba1.json','data/talaba2.json','data/talaba3.json','data/talaba4.json']
for filename in files:
    try:
        with open(filename) as f:
            talaba=json.load(f)
    except FileNotFoundError:
        pass#print(f"{filename} mavjud emas.")
    else:
        print(talaba["ism"])

n=input("Butun son kiriting: ")
try: 
    n=int(n)
    x=20/n
except ValueError:
    print("Siz butun son kiritmadingiz.")
except ZeroDivisionError:
    print("0 ga bo'lish mumkin emas.")
else:
    print(f"x={x}")

while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh=int(yosh)
        break
print(f"Siz {2025-yosh} yilda tug'ilgansiz.")
