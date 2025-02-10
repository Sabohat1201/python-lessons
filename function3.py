#3-shart.Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va
#  asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.
def bahola(ismlar):
        baholar={}
        while ismlar:
            for ism in ismlar:
                baho=input(f"{ism.title()}ning bahosini kiriting: ")
                baholar[ism]=(int(baho))
            break
        return baholar
talabalar=['sabohat','murod','madina','guli']
baholar=bahola(talabalar[:])
print(talabalar)
print(baholar)

#AMALYOT
#1-shart.Matnlardan iborat ro'yxat qabul qilib, 
# ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.
# def katta_harf_qilish(matnlar):
#     matnlar1=[]
#     for n in range(len(matnlar)):
#         matnlar1.append(matnlar[n].capitalize())
#     return matnlar1
# katta_harf=['sabohat','oliy malumotli','madina','o\'rta maxsus']
# matnlar1=katta_harf_qilish(katta_harf[:])
# print(katta_harf)
# print(matnlar1)#Bajarildi
#2-shart. Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va 
# yangi ro'yxat qaytaradigan qilib o'zgartiring
