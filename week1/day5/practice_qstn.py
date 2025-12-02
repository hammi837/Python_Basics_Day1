# qstn01:generate a randon no
import random
print("qstn1:generate a randam no?")
print(f"random no: {random.randint(1,100)}")

#qstn no2:
   # Write a Python program to convert kilometers to miles.
print("qstn2:Write a Python program to convert kilometers to miles?")
kilometers= float(input("enter value in kilometer:"))
# Conversion factor: 1 kilometer = 0.621371 miles
conversion_factor=0.621371
miles=kilometers*conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles")

#qstn no 3:
#crate calender
import calendar
print("qstn3:create a calender?")
year = int(input("Enter year: "))
month = int(input("Enter month: "))

cal = calendar.month(year, month)
print(cal)

#qstn4:
#Write a Python program to swap two variables without temp variable.
print("qstn4:Write a Python program to swap two variables without temp variable?")
a = 5
b = 10
# Swapping without a temporary variable
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)

#qstn no5:
#Write a Python Program to Check if a Number is Positive, Negative or Zero
print(f"qstn no5: Write a Python Program to Check if a Number is Positive, Negative or Zero?")
number=int(input("enter a number:"))
if number > 0:
    print("number is postive")
elif number == 0:
    print("number is zero")
else:
    print("number is negative")

#qstn no6:
# find prime no
def prime(n):
    if n==1:
        print(f"{n} is not a prime no")
    for i in range(2,n):
        if n%i==0:
            print(f"{n} is not a prime no")
            return
    print(f"{n} is a prime no")
print("qstn no6:find a prime number?")
number=int(input("enter a number:"))
prime(number)

#qno7
#FIND FACTORIAL

def factorial(n):
     if n==1:
         return n
     else:
         return n * factorial(n-1)

print("qno7 :FIND FACTORIAL?")
number=int(input("enter a number:"))
print(factorial(number))


#QSTN NO8:
#ASCII VALUE

print("qno7 :FIND ascii value?")
char=str(input("enter a number:"))
print(f"ascii value of {char} is {ord(char)}")




#.......................................qn9:
class FileReader:

    def read_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = file.read()
                return data
        except FileNotFoundError:
            return "Error: File not found."
        except PermissionError:
            return "Error: You don't have permission to read this file."
        except Exception as e:
            return f"Unexpected Error: {e}"


# Using the class
reader = FileReader()

print(reader.read_file("example.txt"))   # If file exists → prints content
print(reader.read_file("numbers.txt"))   # File missing → handled

#.................................qno10
class Calculator:

    def divide(self, a, b):
        try:
            result = a / b
            return f"Result: {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero!"
        except TypeError:
            return "Error: Please enter only numbers."
        except Exception as e:
            return f"Unexpected error: {e}"


# Using the class
calc = Calculator()

print(calc.divide(10, 2))      # Valid division
print(calc.divide(5, 0))       # Division by zero
print(calc.divide("a", 3))     # Invalid input type



#......................qno11

class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self, name, age, subjects):
        try:
            student = {
                "name": name,
                "age": age,
                "subjects": list(subjects)      # Convert tuple/set to list
            }

            self.students.append(student)
            print("Student added successfully!")

        except Exception as e:
            print("Error while adding student:", e)

    def show_students(self):
        try:
            if not self.students:
                print("No students available.")
                return

            for s in self.students:
                unique_subjects = set(s["subjects"])

                print("\n--- Student Info ---")
                print("Name:", s["name"])
                print("Age:", s["age"])
                print("Subjects:", unique_subjects)

        except Exception as e:
            print("Error while showing students:", e)

    def get_student(self, index):
        try:
            student = self.students[index]
            return (student["name"], student["age"], student["subjects"])

        except IndexError:
            print("Error: Invalid student index.")
        except Exception as e:
            print("Unexpected error:", e)

manager = StudentManager()

#use tuple for subjects
manager.add_student("Hammad", 21, ("Math", "Python", "Math"))  

#also use Set works for subjects
manager.add_student("Ali", 22, {"AI", "Python"})  

manager.show_students()

print("\nFetching Student 0:")
print(manager.get_student(0))


