# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
# salom_ber()

# def salom_ber(ism):#ism bu parametr
#     """Foydalanuvchidan ismini so'rab,
#     salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber('sabohat')# sabohat bu argument
# salom_ber('asadbek')

# print(print.__doc__)#Funsiya haqidagi ma'lumotni chiqaradi!

# def toliq_ism(ism,familiya):#ketma ketlikka amal qilish kerak
#     """Foydalanuvchini ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchini ismi: {ism.title()}"
#           f"\nFoydalanuvchi familiyasi: {familiya.title()}")
# toliq_ism('sabohat','qayumova')

# def yosh_hisobla(ism,tugilgan_yil):
#     """Foydalanuvchining yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2025-tugilgan_yil} yoshda!")
# yosh_hisobla('sabohat',2001)#o'rin almashtirmaslik kerak

#KALIT SO'Z BILAN UZATISH
# def yosh_hisobla(tugilgan_yil,ism):
#     """Parametrga qiymat berib hisoblash"""
#     print(f"{ism.title()} {2025-tugilgan_yil} yoshda")
# yosh_hisobla(tugilgan_yil=2001,ism='sabohat')#argument almashsa ham qiymat berilsa xatolik chiqmaydi

#STANDART QIYMAT
# def yosh_hisobla(tugilgan_yil,joriy_yil=2025):#Funksiya yaratishda standart qiymat doim oxirida yozilishi kerak,aks holda xatolik yuz beradi.
#     """Foydalanuvchi tug'ilgan yilida uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz!")
# yosh_hisobla(2001)

def yosh_hisobla(tugilgan_yil,joriy_yil=2025):
    """Foydalanuvchi tug'ilgan yilida uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz!")
t_yil=int(input("Tug'ilgan yilingizni kiriting: "))
yosh_hisobla(t_yil)
