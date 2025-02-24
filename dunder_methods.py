class Avto:
    """Avtomobil klassi"""
    __num_avto=0 #klass xususiyatlari
    def __init__(self,make,model,rang,yil,narx,):
        """Avtomobil xususiyatlari"""
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narx=narx
        Avto.__num_avto+=1
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    def __repr__(self):
        return f"{self.make} {self.model}"
    def __eq__(self,y):
        """Tenglik operatori"""
        return self.narx==y.narx
    def __lt__(self,y):
        return self.narx<y.narx
    def __le__(self,y):
        return self.narx<=y.narx

avto1=Avto("GM","Malibu","Qora",2021,15000)
avto2=Avto("GM","cobolt","Oq",2020,12000)
# print(avto1!=avto2)
# print(avto1>avto2)
# print(avto1>=avto2)

class AvtoSalon:
    """AvtoSalon klassi"""
    def __init__(self,name):
        """AvtoSalon xususiyatlari"""
        self.name=name
        self.avtolar=[]
    def __repr__(self):
        return f"{self.name} avtosaloni"
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting.")
    def __len__(self):
        return len(self.avtolar)
    def __getitem__(self,index):
        return self.avtolar[index]
    def __setitem__(self,index,values):
        if isinstance(values,Avto):
            self.avtolar[index]=values
    def __add__(self,y):
        if isinstance(y,AvtoSalon):
            yangi_salon=AvtoSalon(f"{self.name} {y.name}")
            yangi_salon.avtolar=self.avtolar+y.avtolar
            return yangi_salon
        elif isinstance(y,Avto):
            self.add_avto(y)
        else:
            print(f"AvtoSalon ga {type(y)} ni qo'shib bo'lmaydi.")
    def __call__(self,*qiymat):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]
salon1=AvtoSalon("MaxAvto")
salon2=AvtoSalon("NewAvto")
avto6=Avto("GM","Spark","Oq",2020,7000)
# print(salon1)
salon1.add_avto(avto1,avto2)
print(salon1())
# print(salon1.avtolar)
# print(len(salon1))
# print(salon1[1])
# print(salon1[:])
avto3=Avto("Toyota","Nexia","Qizil",2020,10000)
avto4=Avto("GM","Damas","Oq",2021,8000)
avto5=Avto("Toyota","Lasetti","Qora",2023,12000)
salon2.add_avto(avto1,avto4,avto5)
salon1[0]=avto3
#print(salon1[0])
salon3=salon1+salon2
print(salon3)
salon3+avto6
#print(salon3[:])
avto7=Avto("GM","Matiz","Kulrang",2020,5000)
salon3(avto7)
print(salon3())