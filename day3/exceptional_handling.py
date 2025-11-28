
# exceptional_handling
a=input("enter the number")
print(f"multiplication table of {a} is:") 
try:
   for i in range(1,11):
    print(f"{a} x {i} = {int(a)*i}")
except Exception as e:
    print("error occured:",e)

# handling multiple exception
try:
   num=int(input("enter a number:"))
   a=[10,20,30,40]
   print(a[num]) 
except ValueError:
    print("please enter valid integer number")
except IndexError:
    print("index out of range please enter between 0-3")


# finally block
try:
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))
    result=num1/num2
    print("result is:",result)
except ZeroDivisionError:
    print("division by zero is not allowed")
finally:
    print("execution completed")

# raise keyword
def check_age(age):
    if age<0:
        raise ValueError("age cannot be negative")
    elif age<18:
        print("you are minor")
    else:
        print("you are adult")
try:
    user_age=int(input("enter your age:"))
    check_age(user_age)
except ValueError as ve:
    print("error:",ve)
except Exception as e:
    print("unexpected error:",e)
    