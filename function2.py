# def toliq_ism_yasa(ism,familiya,otasini_ismi=None):#ixtiyoriy argument
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasini_ismi:
#         toliq_ism=f"{ism.title()} {otasini_ismi.capitalize()} {familiya.title()}"
#     else:
#         toliq_ism=f"{ism.title()} {familiya.title()}"
#     return toliq_ism
# talaba1=toliq_ism_yasa('sabohat','qayumova')
# talaba2=toliq_ism_yasa('murod','qayumov','Abduvali o\'g\'li')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

def avto_info(kompaiya,model,rangi,korobka,yili,narxi=None):
    avto={
        'kompaniya':kompaiya,
        'model':model,
        'rang':rangi,
        'korobka':korobka,
        'yil':yili,
        'narx':narxi
    }
    return avto
# avto1=avto_info('gm','malibu','qora','avtomat',2018,15000)
# avto2=avto_info('gm','cobolt','oq','mexanika',2020)
# avtolar=[avto1,avto2]
# print("Onlayn bozordagi mavjud mashinalar: ")
# for avto in avtolar:
#     if avto['narx']:
#         narx=avto['narx']
#     else:
#         narx='Nomalum'
#     print(f"{avto['rang'].title()} {avto['model']}. Narxi: {narx}")

# def oraliq(min,max,qadam=None):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         if qadam:
#             min += qadam
#         else:
#             min += 1
#     return sonlar
# print(oraliq(0,10, 4))
# print(oraliq(10,21))#Bajareildi

print("Saytdagi avtolar ro'yhatini shakllantiramiz.")
avtolar=[]
while True:
    print("\nQuyidagi ma'lumotlarni kiriting: ")
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rang=input("Rangi: ")
    korobka=input("Korobkasi: ")
    yil=input("Yili: ")
    narx=input("Narxi: ")
    avtolar.append(avto_info(kompaniya,model,rang,korobka,yil,narx))
    javob=input("Yana avto qo'shasizmi? (yes/no): ")
    if javob == 'no':
        break