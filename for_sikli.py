mehmonlar=['sabohat','olim','madina','guli','asadbek','murod']
for mehmon in mehmonlar:
    print("Salom,", mehmon.capitalize())
    print("Xayr,", mehmon.title())
    print(f"Assalomu alekum {mehmon.title()} sizni oshga taklif etamiz")
sonlar=list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")
#dostlar=[]
#print("5 ta yaqin do'stingizni ismini kiriting")
#for n in range(5):
#    dostlar.append(input(f"{n+1} do'stingizni ismini kiriting\n>>>"))
#print(dostlar)


toq_sonlar=list(range(11,100,2))
for son in toq_sonlar:
    print(f"{son} ning kubi {son**3} ga teng")

suhbat_qilinganlar=[]
suhbat = range(int(input("Bugun necha kishini subat qildingiz?\n>>>")))
for n in suhbat:
    suhbat_qilinganlar.append(input(f"{n+1} - suhbat qilgan odamingiz kim edi: "))
print(suhbat_qilinganlar)