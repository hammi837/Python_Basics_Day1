#................File Handling in Python..............

# replace the word "python" with "java" in a text file
with open('example.txt', 'w') as f:
    f.write("hi everyone\nmy name is hammad hafeez\nI am learning file handling in python")
with open('example.txt', 'r') as f:
    data=f.read()
    new_data=data.replace("python","java")
    print(new_data)
with open('example.txt', 'w') as f:
    f.write(new_data)

# find a word in a text file 
word_to_find = "learning"
with open('example.txt', 'r') as f:
    data=f.read()
    if (data.find(word_to_find) != -1):
       print(f"The word '{word_to_find}' is found in the file.")
    else:
         print(f"The word '{word_to_find}' is not found in the file.")

# find the line number of a specific word (learning) occur first in a text file
#word_to_find = "learning"
#data=True
#line_no=1
#with open('example.txt', 'r') as f:
   # while data:
    #  data=f.readlines()
   #        print(line_no)
 #     line_no+=1
#


# find even no in a text file and write them to another file
with open('numbers.txt', 'w') as f: 
    for i in range(1, 10):
        f.write(f"{i},")   
    f.write("10")  
with open('numbers.txt', 'r') as f:
    count=0
    data=f.read()
    nums=data.split(',')
    print(nums)
    for value in nums:
        if (int(value) % 2 == 0):
            count+=1
print("even numbers in file:",count)



#....................................... json file handling 
# read json file           
import json

with open('student.json', 'r') as f:
    data=f.read()
    finaldata=json.loads(data)
    print(finaldata)
    print(type(finaldata))

# write json file
with open('employee.json', 'w') as f:
    emp_data={
        "emp_id":101,
        "emp_name":"john",
        "emp_dept":"hr"
    }
    json_data=json.dumps(emp_data,indent=4)
    f.write(json_data)





  

#......................csv file handling
# read csv file
import csv
with open('students.csv', 'r') as f:
    reader_obj=csv.reader(f,delimiter=',')
    print(type(reader_obj))
    for row in reader_obj:
        print(row)

# write csv file
# wo.writerow for single row
# wo.writerows for multiple rows
with open('employees.csv', 'w') as f:
    writer_obj=csv.writer(f,delimiter=',')
    writer_obj.writerow(['emp_id','emp_name','emp_dept'])
    writer_obj.writerow([101,'john','hr'])
    data=[[102,'alice','it'],
          [103,'bob','finance']]
    writer_obj.writerows(data)
    

     
      