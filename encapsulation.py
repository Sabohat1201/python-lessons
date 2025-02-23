from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    __num_avto=0 #klass xususiyatlari
    def __init__(self,make,model,rang,yil,narx,km=0):
        """Avtomobil xususiyatlari"""
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narx=narx
        self.__km=km #Inkapsulyatsiya
        self.__id=uuid4()
        Avto.__num_avto+=1
    def get_km(self):
        return self.__km
    def get_id(self):
        return self.__id
    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km+=km
        else:
            print("Mashina km ga kamaytirib bo'lmaydi")
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
avto1=Avto("GM","Malibu","Qora",2021,15000,1000)
avto2=Avto("GM","cobolt","Oq",2020,12000,1500)
avto1.add_km(2000)
print(Avto.get_num_avto())
print(avto1.get_km())
