talaba={
    'ism':'Sabohat',
    'familiya':'Qayumova',
    'yosh':24,
    'fakultet':'Telekomunikatsiyalar',
    'kurs':4
}
# print(talaba.items())
# for key,value in talaba.items():
#     print(f"Kalit:{key}")
#     print(f"Qiymat:{value}\n")

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
# for k,q in telefonlar.items():
#     print(f"{k.title()}ning telfoni {q}.")

mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }
# print(mahsulotlar.keys())
# for mahsulot in mahsulotlar.keys():
#     print(f"{mahsulot.title()}ning narxi {mahsulotlar[mahsulot]} so'm.")
# print("Do'kondagi mahsulotlar:")
# for mahsulot in mahsulotlar:
#     print(mahsulot)
# buyurmalar=['anjir','non','anjir','baliq']
# for mahsulot in buyurmalar:
#     if mahsulot not in mahsulotlar:
#         print(f"Iltimos do'koningizga {mahsulot} ham olib keling")

# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

print("Foydalanuvchilar quyidagi telfonlarni ishlatishadi: ")
# for tel in telefonlar.values():
#     print(tel)

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }
telefon=set(telefonlar.values())
for tel in sorted(telefon):
    print(tel)
    
mevalar={'olma','mandarin','banan','gilos'}