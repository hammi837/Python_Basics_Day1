def calculator():
    print("\n=== Calculator ===")
    print("enter 1 for addition")
    print("enter 2 for subtract")
    print("enter 3 for multiplication")
    print("enter 4 for division")
    print("enter 5 for without decimal point")
    print("enter 6 for find reminder")
    print("enter 7 for power")
    print("enter 8 for exit")
    while True:
         check=int(input("enter valid number which operatuon u perform "))
         if check==8:
            print("exiting Calculator")
            break
         num1 = int(input("Enter your  no1: "))
         num2 = int(input("Enter your no2: "))
         print("\n")
         if  check==1:
           print("addition of",num1,"and",num2,"is",num1+num2)
         elif  check==2:
           print("subtract of",num1,"and",num2,"is",num1-num2)
         elif check==3:
           print("multiply of",num1,"and",num2,"is",num1*num2)
         elif  check==4:
           print("division of",num1,"and",num2,"is",num1/num2)
         elif  check==5:
           print("division without decimal of",num1,"and",num2,"is",num1//num2)
         elif check==6:
           print("reminder of",num1,"and",num2,"is",num1%num2)
         elif   check==7:
           print("power of",num1,"and",num2,"is",num1**num2)
         else:
           print("Invalid choice. Please try again.")




def unit_converter():
   print("\n=== unit converter ===")
   print("enter 1 for km to meter")
   print("enter 2 for meter to km")
   print("enter 3 for cm to meter")
   print("enter 4 for meter to cm")
   print("enter 5 for meter to milimeter")
   print("enter 6 for milimeter to meter")
   print("enter 7 for exit")
   while True:
         check=int(input("enter valid number which u perform "))
         if check==7:
            print("exiting unit_converter")
            break
         num1 = int(input("Enter your number: "))
         print("\n")
         if  check==1:
           print("convert km to meter",float(num1)*1000)
         elif  check==2:
           print("convert meter to km",float(num1)/1000)
         elif check==3:
           print("convert cm to meter ",float(num1)/100)
         elif  check==4:
           print("covert meter to cm",float(num1)*100)
         elif  check==5:
           print("convert cm to milimeter",float(num1)*10)
         elif check==6:
           print("convert milimetr to cm",float(num1)/10)
         else:
           print("Invalid choice. Please try again.")
   




print("\n====== MAIN MENU ======")
print("Enter 1 for using Unit Converter")
print("Enter 2 for using Calculator")
print("Enter 3 for  Exit the program")
while True:
        option = input("Choose an option: ")
        if option == "1":
            unit_converter()
        elif option == "2":
            calculator()
        elif option == "3":
            print("Exiting program!")
            break
        else:
            print("Invalid choice. Please try again.")
