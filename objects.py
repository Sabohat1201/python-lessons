class Student:
    def __init__(self,name,lastname,y_of_birth):
        self.name=name
        self.lastname=lastname
        self.years_of_birth=y_of_birth
        self.year=1
    def set_year(self,new_year):
        """Talabaning bosqichini yangilaydigan metod"""
        self.year=int(new_year)
    def update_year(self):
        """Talabaning bosqichini 1 taga ko'paytirish"""
        self.year+=1
    def get_name(self):
        return self.name
    def get_lastname(self):
        return self.lastname
    def get_age(self,year):
        return year-self.years_of_birth
    def introduce(self):
        return f"Men {self.lastname} {self.name}, {self.years_of_birth} - yil tug'ilganman.{self.year} - bosqich talabasi"
    def get_fullname(self):
        """Talaba haqida malumot"""
        return f"{self.name} {self.lastname} "
    
student1=Student("Sabohat","Qayumova",2001)
student2=Student("Madina","Bobomurodova",1995)
# print(student1.year)
# student1.update_year()
# student2.set_year(4)
# print(f"{student1.year} {student2.year}")
class Science:
    """Fan nomli klass"""
    def __init__(self,name):
        self.name=name
        self.number_of_students=0
        self.students=[]

    def add_students(self,talaba):
        """Fanga talabalar qo'shing"""
        self.students.append(talaba)
        self.number_of_students+=1
  
    def get_students(self):
        return [student.get_fullname() for student in self.students]

matem=Science("Oliy matematika")
matem.add_students(student1)
matem.add_students(student2)
matematika=matem.get_students()
print(matematika)
print(matem.number_of_students)

#DUNDER metodlar
#print(dir(Student))
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]
print(see_methods(Student))
print(see_methods(Science))
print(student1.__dict__)
print(student1.__dict__.keys())