#oop concept

#..............class  and object
class Student:
    name="hammad"    
s1=Student()
print(s1.name)

#...............constructor
# constructor object ke initilazation ka lia hoata hn
class Student:
    def __init__(self):              # self point object (self and object same think)
        self.name="hammad"
    
s1=Student()
print(s1.name)

#..............parameterized constructor
class Student:
    collage_name="pgc"
    name="anaymus"
     #parameter constructors
    def __init__(self ,fullname,marks):
        self.name=fullname           #self.name created in object as a variable
        self.marks=marks
        print("adding new student")
            
          
s1=Student("hammad",78)
print(s1.name,s1.marks)

s2=Student("ali",89)
print(s2.name,s2.marks)
print(s2.collage_name)

# 4 pillars of OOP

#...................................1. abstraction.....................................
#abstraction: hiding the implementation of class (unnessary features)
#             and showing the essiential(important) feature of class
#example: like we start the car and like we show key point,break,gear,(essiantial feature)
#         but hum hama nhii pata engine ma kia ho raha hn koe ka usa hide kia gia hn (unnessary for user)


# see abstarction dont show acc,clutch,brk jut show car started
class car:
    def __init__(self):
        self.acc=False
        self.clutch=False
        self.brk=False
    def start(self):
        self.acc=True
        self.clutch=True
        print("car started.............")
                
s1=car()
s1.start()


#...................................2. encapsulation.....................................
#Encapsulation
#   capsule of data and related func
#     wrapping data and func into single unit(object)

class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc
    def credit(self,amount):
        self.balance+=amount
        print("this",amount ,"credit from ur account")
        print("total balnce",self.balance)
    def debit(self,amount):
        self.balance-=amount
        print("this",amount ,"debit from ur account")
        print("total balnce",self.balance)
        
acc1=account(5000,12345)
acc1.credit(1000)
acc1.debit(500)
acc1.credit(1000)
acc1.credit(1000)

#  qtsn no2:

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass    #use double score to private the acc_password attribute
    def reset_pass(self):
        print(self.__acc_pass)

acc1=Account("a1234","abc1123")
print(acc1.acc_no)
print(acc1.reset_pass)



#...................................3. inheritance.....................................

# single inheritance
class Car:
    color="black"
    @staticmethod
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("car stopped....")
class Toyotacar(Car):
    def __init__(self,name):
        self.name=name
        
car1=Toyotacar("fortuner")
car1=Toyotacar("prius")

print(car1.name)
print(car1.start())
print(car1.color)
print(car1.stop())




