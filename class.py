class Student:
    def __init__(self,name,lastname,y_of_birth):
        self.name=name
        self.lastname=lastname
        self.years_of_birth=y_of_birth
    def get_name(self):
        return self.name
    def get_lastname(self):
        return self.lastname
    def get_age(self,year):
        return year-self.years_of_birth
    def introduce(self):
        return f"Men {self.lastname} {self.name}, {self.years_of_birth} - yil tug'ilganman."
    
student1=Student("Sabohat","Qayumova",2001)
student2=Student("Madina","Bobomurodova",1995)
# print(student1.get_name())
# print(student1.get_age(2025))
# print(student2.introduce())
# print(student1.introduce())

#AMALYOT
class User:
    """Foydalanuvchi haqida malumot beruvchi klass"""
    def __init__(self,name,username,lastname,email):
        """Klassning xususiyatlari"""
        self.name=name
        self.username=username
        self.lastname=lastname
        self.email=email
    def get_info(self):
        """Foydalanuvchi ma'lumotlarini chiqaruvchi funksiya"""
        return f"Foydalanuvchi: {self.name}\nIsmi: {self.username.title()} {self.lastname.title()}\nEmail: {self.email}"
user1=User("sabohat1201","sabohat","qayumova","saboxatqayumova7@gmail.com")
print(user1.get_info())