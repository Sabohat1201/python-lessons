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
def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
    avtolar=[]# salondagi avtolar uchun bo'sh ro'yxat
    while True:
        print("\n Quyidagi ma'lumotlarni kiriting:", end=' ')
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
    print(avtolar)
def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narx']}$")