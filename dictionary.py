car_0={'model':'ferrari','rang':'qizil'}
#print(car_0['model'])
en_uz={'apple':'olma','apricot':"o'rik",'banana':'banan'}
#print(en_uz)
en_uz['strawberry']='qulupnay'
#print(en_uz)
talaba={
    'ism':'qayumova sabohat',
    'yosh':24,
    't_yil':2001
}
#print(f"Talaba {talaba['ism'].title()} {talaba['t_yil']} - yil, {talaba['yosh']} yoshda")
del talaba['yosh']
#print(talaba)
talaba['ism']='murod qayumov'
talaba['t_yil']=1993
#print(f"Talaba {talaba['ism'].title()} {talaba['t_yil']} - yil.")
talaba_1={
    'ism':'qayumova sabohat',
    't_yil':2001
}
talaba_1['kurs']=4
talaba_1["yo'nalish"]='telekomunikatsiyalar'
# print(f"Talaba {talaba_1['ism'].title()}\
#  {talaba_1['t_yil']} - yil,\
#  {talaba_1['kurs']} -kurs talabasi,\
#  {talaba_1['yo\'nalish']} yo'nalishida o'qiydi")
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
#phone=telefonlar.get('sabohat','Bu ism mavjud emas')
phone=telefonlar.get('ali')
#print(phone)


#Amalyot
sonlar={
    'integer':'butun son',
    'float':"o'nlik son",
    'string':'matn'}
k_kirit=input("Kalit so'zini kiriting: ")
#print(sonlar.get(k_kirit,"Bunday so'z mavjud emas."))
tarjima=sonlar.get(k_kirit)
if tarjima == None:
    print("Bunday so'z mavjud emas.")
else:
    print(f"{k_kirit.title()} so'zi {tarjima} deb tarjima qilinadi.")