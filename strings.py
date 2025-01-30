ism="Sabohat"
shahar='Toshkent'
viloyat="Qashqadaryo"
matn = "Men yangi 📱 oldim"
print(matn)
print(f"Mening ismim {ism.title()}, men hozir {shahar.capitalize()} shahrida yashayapman.\n\t Men {viloyat.capitalize()} viloyatida tug'ilganman va {matn.lower()}")
familiya="Qayumova"
print(ism +' '+familiya)
ism_sharif=f"{ism} {familiya}"
print(ism_sharif)
matn2="    Men maktabga bormayapman       "
print(matn2.lstrip())
print(matn2.rstrip())
print(matn2.strip())
ism= input("Ismingiz nima?\n>>>")
print("Assalomu alaykum," + ism.title())