#........inheritance.........

#1. Single Inheritance:
#   One child class inherits from one parent class

class Parent:
    def show_parent(self):
        print("This is Parent class.")

class Child(Parent):
    def show_child(self):
        print("This is Child class.")

c = Child()
c.show_parent()
c.show_child()

#2. Multi-level Inheritance:
#   A child class inherits from a parent class, 
#   and then another class inherits from that child class.

class GrandParent:
    def show_gp(self):
        print("This is Grandparent.")

class Parent(GrandParent):
    def show_parent(self):
        print("This is Parent.")

class Child(Parent):
    def show_child(self):
        print("This is Child.")

c = Child()
c.show_gp()
c.show_parent()
c.show_child()

#3. Multiple Inheritance:
#   A child class inherits from more than one parent class.

class Father:
    def skills(self):
        print("Father skills: Driving")

class Mother:
    def skills(self):
        print("Mother skills: Cooking")

class Child(Father, Mother):
    def child_skills(self):
        print("Child skills: Painting")

c = Child()
c.skills()         # Executes Father first (MRO)
c.child_skills()

#Hierarchical Inheritance:
     #One parent → many child classes.

class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def dog_sound(self):
        print("Dog barks")

class Cat(Animal):
    def cat_sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
d.dog_sound()

c.sound()
c.cat_sound()



#Hybrid Inheritance (Combination):
#Combination of multiple types.
#Example: mix of hierarchical + multiple inheritance.

class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(A):
    def showC(self):
        print("Class C")

class D(B, C):  # Hybrid structure
    def showD(self):
        print("Class D")

d = D()
d.showA()
d.showB()
d.showC()
d.showD()


