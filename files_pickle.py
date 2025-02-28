#1 - usul
# file=open('data/pi.txt')
# PI=file.read()
# print(PI)
# file.close()
#2 - usul
with open('data/pi.txt') as file:
    pi=file.read()
    pi=pi.rstrip()
    pi=pi.replace('\n','')#bir belgigi ikkinchisiga almashtirish
    pi=float(pi)
#print(type(pi))
#Papka ichidagi fayllarni ochish
with open('data/pi.txt') as file:
    pi=file.read()
#print(pi)
ism="Sabohat Qayumova"
tyil=2001
with open('data/talabalar.txt','w') as file:
    file.write(ism+"\n")
    file.write(str(tyil)+"\n")#Matnga o'tkazish shart
with open('data/talabalar.txt','a') as file:
    file.write("Murod Qayumov"+"\n")
    file.write("1993"+"\n")
with open('data/talabalar.txt','a') as file:
    file.write("Madina Bobomurodova"+"\n")
    file.write("1995"+"\n")
with open('data/talabalar.txt','a') as file:
    file.write("Olim Eshqobilov"+"\n")
    file.write("1991"+"\n")
#print(type(file))
#print(file)
filename="data/talabalar.txt"
# with open(filename) as file:
#     for line in file:
#         print(line)
with open(filename) as file:
    talabalar=file.readlines()#Ro'yhat ko'rinishda saqlaydi
    talabalar= [talaba.rstrip() for talaba in talabalar]
print(talabalar)

#O'zgaruvchilarni saqlash PICKLE - faqat dastur ichida ishlaydi.
import pickle
talaba1={'ism':'Sabohat','familiya':'Qayumova','tyil':2001,'kurs':3}
talaba2={'ism':'Madina','familiya':'Bobomurodova','tyil':1995,'kurs':4}
with open('info','wb') as file:#write binary - ikkilik sanoq sistemasida yozish
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)
with open('info','rb') as file:# read binary-o'qish
    talaba1=pickle.load(file)
    talaba2=pickle.load(file)
print(talaba1)
print(talaba2)