car_0={
    'model':'lasetti',
    'rang':'oq',
    'yil':2018,
    'narh':13000,
    'km':50000,
    'korobka':'avtomot'
}
car_1={
    'model':'nexia 3',
    'rang':'qora',
    'yil':2013,
    'narh':9000,
    'km':89000,
    'korobka':'mexanika'
}
car_2={
    'model':'gentra',
    'rang':'qizil',
    'yil':2019,
    'narh':15000,
    'km':20000,
    'korobka':'mexanika'
}
# car=car_0
# print(f"{car['model'].title()},\
#     {car['rang']} rang,\
#     {car['yil']} - yil, {car['narh']}$")
# car=car_1
# print(f"{car['model'].title()},\
#     {car['rang']} rang,\
#     {car['yil']} - yil, {car['narh']}$")
# car=car_2
# print(f"{car['model'].title()},\
#     {car['rang']} rang,\
#     {car['yil']} - yil, {car['narh']}$")

cars=[car_0,car_1,car_2]
# for car in cars:
#     print(f"{car['model'].title()},\
#     {car['rang']} rang,\
#     {car['yil']} - yil, {car['narh']}$")

# print(cars[0])
# print(cars[0]['model'])
# print(f"{cars[0]['rang'].title()} "
#       f"{cars[0]['model']}")

malibues=[]
for n in range(10):
    new_car={
        'model':'malibu',
        'rang':None,
        'yil':2020,
        'narh':None,
        'km':0,
        'korobka':'avto'
    }
    malibues.append(new_car)
#print(malibues)

for malibu in malibues[:3]:
    malibu['rang']='qizil'

for malibu in malibues[3:6]:
    malibu['rang']='qora'

for malibu in malibues[6:]:
    malibu['rang']='qora',
    malibu['korobka']='mexanik'

#print(malibues)

for malibu in malibues:
    if malibu['korobka']=='avto':
        malibu['narh']=40000
    else:
        malibu['narh']=35000
#print(malibues)

dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

# for key, values in dasturchilar.items():
#     print(f"\n{key.title()} quyidagi dasturlash tillarini biladi: ", end='')
#     for til in values:
#         print(f"{til.upper()}", end=' ')

hamkasblar = {
    'sabohat':{
        'familiya':'qayumova',
        't_yil':2001,
        'ma\'lumoti':'oliy',
        'tillar':['python','html']
    },
    'murod':{
        'familiya':'qayumov',
        't_yil':1993,
        'ma\'lumoti':'oliy',
        'tillar':['css','javascript']
    },
    'madina':{
        'familiya':'bobomurodova',
        't_yil':1995,
        'ma\'lumoti':'oliy',
        'tillar':['django','c#']
    }
}
for k,q in hamkasblar.items():
    print(f"\n{k.title()} {q['familiya'].title()} " 
          f"{q['t_yil']} - yil. "
          f"Ma'lumoti {q['ma\'lumoti']}")
    print("Quyidagi dasturlash tillarini biladi: ", end=' ')
    tillar=q['tillar']
    for til in tillar:
        print(f"{til.upper()}", end=' ')