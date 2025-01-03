# area_of_circle = lambda pi,r: pi*(r*r)
# perimeter_of_circle = lambda pi,r: (2*pi)*r
# volume_of_sphere = lambda pi,r: 4/3*pi*(r**3)
# perimeter_of_triangle = lambda a,b,c: a+b+c
# area_of_triangle = lambda h,b: (h*b)//2

# def main(func1,func2,func3,func4,func5):
#     value1=float(input("enter the value first:"))
#     value2=int(input("enter the value second:"))
#     value3=int(input("enter the value third:"))
#     value4=int(input("enter the value fourth:"))
#     value5=int(input("enter the value fifth:"))
#     value6=int(input("enter the value sixth:"))
#     print(func1(value1,value2))
#     print(func2(value1,value2))
#     print(func3(value1,value2))
#     print(func4(value3,value4,value5))
#     print(func5(value4,value6))

# main(area_of_circle,perimeter_of_circle,volume_of_sphere,perimeter_of_triangle,area_of_triangle)
# list1=[]
# list2=list("hello")
# list3=[]
# num=int(input("enter the number:"))
# list3.append(num)
# print(list3)
# for i in range(5):
#     list3.append(i)
#     print(list3)
# list1=[]
# for i in range(10):
#     num=int(input("enter the numbers:"))
#     list1.append(num)
# user=input("enter the number for count:")
# counted=list1.count(user)
# print("the number appeared times:",counted)

# list2=[1,10,23,45,2,7,0,3,4]
# list2.sort()
# print(list2[-2])
# minimum=min(list2)
# maximum=max(list2)
# print(minimum)
# print(maximum)
# numbers=[1,10,23,45,2,7,0,3,0,4]
# even_numbers=[num for num in numbers if num %2==0]
# odd_numbers=[num for num in numbers if num%2!=0]

# print("even number:",even_numbers)
# print("odd numbers",odd_numbers)
# def even_odd_count():
#     list1 = [1,23,45,2,7,0,3,4]
#     even = 0
#     odd = 0
#     for i in list1:
#         if i%2==0:
#             even += 1
#         else:
#             odd +=1
#         print(even,odd)
# even_odd_count()

# first_text = (input("enter your string:"))
# text = first_text.split(" ")
# reverse_statement = []
# for word in text:
#      reverse = word[::-1]
#      reverse_statement.append(reverse)

# reverse_characters = ' '.join(reverse_statement)
# print(f"your actual string was:{text}")
# print(f"the reversed string is:{reverse_characters}")

# string="hello hi"
# text=string.split(" ")
# text.reverse() 
# reverse_text = " ".join(text)
# print(f"your string was:{string}")
# print(f"your reversed string is:{reverse_text}")

# name=input("enter the fruit name:")
# quantity=int(input("enter the quantity of fruit:"))
# price=int(input("enter the price of fruit:"))

# fruits={"fruit_name":name,"fruit_quantity":quantity,"fruit_price":price}
# print(fruits)
# items = []
# user = int(input("enter the number of item:"))
# for i in range(user):
#     item_name = input("please enter the name of item")
#     item_price = input("please enter the price of item")
#     item_quantity = input("please enter the quantity of item")

#     item_map ={"Name":item_name,"Price":item_price,"Quantity":item_quantity}
#     items.append({"Name":item_name,"Price":item_price,"quantity":item_quantity})

# for i in items:
#     print(f"""the item{i.get("Name")} is of price : {i.get("Price")} and it's quantity is :{i.get("Quantity")}""")
#     print(items)
# from random import *
# num = randint(1,100)
# user_num = int(input("enter the guessing number:"))
# for i in range(10):

#     if user_num==num:
#      print("your guessed the number corret!")
#      elif user_num>num:
#         print("your number is greater")
#         break 

#     else:
#      print("you lose the number was:{num}")
# print(num)
# def levels():
#     print("""welcome to number guessing game!
#     choose your level:
#     1. easy(1 to 10)
#     2.medium(1 to 50)
#     3.hard(1 to 500)
#     4.impossible(1 to 5000)
#     5.exit""")
#     choice = int(input("enter your level in number:"))
#     while True:
#         if choice == 5:
#             print("bye")
#             break
#         if choice == 1:
#             num == randint(1,10) 
#             return num
#         elif choice == 2:
#             num == randint(1,50)
#             return num
#         elif choice == 3:
#             num == randint(1,500)
#             return num
#         elif choice == 4:
#             num == randint(1,5000)
#             return num,chance
#         else:
#             print("invalid")
#             break
# def main_game():
#     num,chance = levels()
#     for i in range(chance):
#         user_input = int(input("enter the guessing number:"))
#         if user_input == num:
#             print(f"you guessed it right number and in{i} chances")
#             break
#         elif user_input > num:
#             print("your number is greater than the actual number")
#         elif user_input < num:
#             print("your number is smaller than the actual number")
    #       else:
    #         print("inavalid number")
    # else:
    #     print(f"you lose the game! the number was : {num}")
# def factorial_recursive(n):
#     if not isinstance(n,int):
#         raise TypeError("input must be an integer.")
#         if n < 0 :
#             raise ValueError("input must be a non-negative integer.")
#         elif n == 0 or n == 1
#             return 1
#         else:
#             return n* factorial_recursive(n-1)
# n = int(input("enter a number:"))
# result = factorial_recursive(n)
# print(f"factorial of {n}: {result}")

#factorial of a number (using recursion)
# def recur_factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n*recur_factorial(n-1)
# num = int(input("enter a number:"))
# if num < 0:
#     print("sorry, factorial does not exist for negative numbers")
# elif num == 0:
#     print("the factorial of 0 is 1")
# else:
#     print("the factorial of",num,"is",recur_factorial(num))
#without using recursion
# n=int(input("enter a number:"))
# fact=1
# while(n>0):
#     fact=fact*n
#     n=n-1
# print("factorial of the number is:")
# print(fact)
# def palindrome(string):
#     original_string = string.strip().lower()
#     reverse_string = original_string[::-1]
#     if original_string == reverse_string:
#         return True
#     else:
#         return False
# string = input("enter your string:")
# result = palindrome(string)
# if result:
#     print("palindrome")
# else:
# #     print("not palindrome")
# from random import choice
# inputs = ["rock","paper","scissor"]

# c_score = 0
# p_score = 0
# chances = 0
# while chances<5:
#     computer = choice(inputs)
#     player = input("enter your choice(rock,paper,scissor)").lower()
#     if computer == player:
#         print("both tied")
#         p_score += 5
#         c_score += 5
#         chances += 1
#     elif player == "rock" and computer == "scissor":
#      print("player won")
#      p_score += 10
#      chances += 1
#     elif player == "paper" and computer == "rock":
#        print("player won")
#        p_score += 10
#        chances += 1
#     elif player == "scissor" and computer == "paper":
#        print("player won")
#        p_score += 10
#        chances += 1
#     elif computer == "rock" and player == "scissor":
#        print("computer won")
#        c_score += 10
#        chances += 1
#     elif computer == "paper" and player == "rock":
#        print("computer won")
#        c_score += 10
#        chances += 1
#     elif computer == "scissor" and player == "paper":
#        print("computer won")
#        c_score += 10
#        chances += 1 
#     else:
#        print("invalid move!")
#        chances += 1
# else:
#    if p_score > c_score:
#       print("player won the match!")
#    elif p_score< c_score:
#       print("computer won the match!")
#    else:
#       print("both the tied!")
#dice rolling      
# from random import choice 
# faces =[1,2,3,4,5,6]
# turns = int(input("enter the turns : "))
# c_score = 0
# p_score = 0
# for _ in range(turns):
#     computer = choice(faces)
#     player = choice(faces)
#     print(f"Computer Dice : {computer} and Player Dice : {player}")
#     if computer>player:
#         print("computer won")
#         c_score += 10
    
#     elif player>computer:
#         print("player won")
#         p_score += 10
#     elif computer == player:
#         print("both tied")
#         c_score += 5
#         p_score += 5
# else:
#     if c_score>p_score:
#         print("computer won the match!")
#         print(f"Computer score:{c_score} and player score: {p_score}")
#     elif c_score < p_score:
#         print("player won the match!")
#         print(f"computer score :{c_score} and player score:{p_score}")
#     else:
#         print("both tied")    
#         print(f"computer score:{c_score} and player score:{p_score}")
        
# #stack and queues
# """stacks-lifo model
# queues-fifo model"""
# cart = []
# def push(cart):
#     item = input("enter the item to add:")
#     cart.append(item)
# def pop(cart):
#     cart.pop()
# def is_empty(cart):
#     if not cart:
#         print("cart is empty")
#     else:
#         print("cart is not empty")
# def peek(cart):
#     if not cart:
#         print("cart is empty")
#     else:
#         last_item = cart[-1]
#         print(f"the last item is : {last_item}")
# def display(cart):
#     if not cart:
#         print("cart is empty")
#     else:
#         print(cart)
# def main():
#     print("""choice :
#         1.add an item
#         2.remove an item
#         3.peek an item
#         4.display full cart
#         5.check cart if it is empty 
#         6.exit""")
#     while True:
#         choice = int(input("enter your choice:"))
#         if choice == 6:
#             print("program exited!")
#             break
#         if choice == 1:
#             push(cart)
#         elif choice == 2:
#             pop(cart)
#         elif choice == 3:
#             peek(cart)
#         elif choice == 4:
#             display(cart)
#         elif choice == 5:
#             is_empty(cart)
#         else:
#             print("invalid")
#             break

# main()

# line = []
# def enqueue(line):
#     person = input("enter the name of person:")
#     line.append(person)
# def dequeue(line):
#     if not line:
#         print("line is empty")
#     else:
#         line.pop(0)
# def display(line):
#     if not line:
#         print("line is empty")
#     else:
#         print(line)
# def show_first(line):
#     if not line:
#         print("line is empty")
#     else:
#         first = line[0]
#         print(f"the first person is :{first}")
# def is_empty(line):
#     if not line:
#         print("line is empty")
#     else:
#         print("line is not empty")
# def main():
#     print("""choice:
#        1. add a person
#        2. remove a person
#        3.display the person name
#        4.show first person in line
#        5.show if line is empty
#        6. exit""")
#     while True:
#         choice = int(input("enter the choice:"))
#         if choice == 6:
#             print("program exited!")
#             break
#         if choice == 1:
#             enqueue(line)
#         elif choice == 2:
#             dequeue(line)
#         elif choice == 3:
#             display(line)
#         elif choice == 4:
#             show_first(line)
#         elif choice == 5:
#             is_empty(line)
#         else:
#             print("invalid!")
#             break
# main()
#to do list
# tasks=[]
# def add_task():
#     task=input("enter the ")
# def display():
#     if not tasks:
#         print()
#     for index,task in enumerate(task,start=1):
#         print(f"")

# def remove_task():
#     if not tasks:
#         print("list is empty")
#     else:
#         display()
#         pos=int(input())
#         tasks.pop(pos-1)
# def main():
#list comprehesion
# list1 = [1,2,3,22,33,44,55,66,777]
# list2 = [x**2 for x in range(88)if x%3==0]
# print(list2)
# list1=[1,2,3,4,5,6,7,8]
# double=list(map(lambda x: x**2,list1))
# print(double)
# list2=["radhika","pooja","kajal"]
# print("enter the name you want to add in list:")
# for _ in range(5):
#     name=input("enter the name")
#     list2.append(name)
# Title=list(map( str.title,list2))
# print(Title)

# list3=[x for x in range(1,91)]

# lower=list((filter(lambda x:x%3==0,list3)))
# print(lower)
# def load_questions():
#     return [
#             {"question":"kon banega crorepati?",
#             "options": ["1.Kajal","2.Pooja","3.Amitabh","4.Rekha"],
#             "answer":"4" 
#             },
#             {"question":"kya kajal pagal hai?",
#             "options": ["1.ha","2.nhi","3.bilkul hai","4.bhot jyada hai"],
#             "answer":"4"
#             },
            
#             {"question":"apoorav bhaiya kiske sath date par jayenge?",
            
#             "options":["1.shreya","2.arpita","3.shreshtha","4.madhav"],
#             "answer":"4"
#             },
#             {"question":"chhutti kab hogi?",
#             "options":["1.subah","2.shaam","3.raat","4.kal"],
#             "answer":"2"
#             },
#             {"question":"kajal ki height kitni hai?",
#             "options":["1.4","2.5'2","3.keede jitni","4.mohit bhaiya k tilak jitni"],
#             "answer":"4"
#             }
#         ]

# def ask_question(question):
#     print("Question aapki computer screen ke saamne : ", question["question"], "\n")
#     print("Options aapki computer screen pe yeh pade")
#     for options in question["options"]:
#         print(options)

#     while True:
#         answer = input("Jawaab lock kare : ")
#         if answer in ['1','2','3','4']:
#             return answer
#         else:
#             print("Galat Jawaab") 



# def main():
#     print("Dewiyon aur Devtao swagat hai aapka kon banega roadpati me")
#     questions = load_questions()
#     paisa = 0

#     for question in questions:
#         answer = ask_question(question)
#         if answer == question['answer']:
#             print("Sahi Jawaab")
#             paisa += 1000
#         else:
#             correct = question['options'][int(question['answer'])-1]
#             print(f"oh no galat jawaab sahi jawaab aapki computer screen par ye raha {correct}")
    
#     print(f"App Jitee hai : {paisa} aapke bank account ka password dijiye")
#     print("Paisa jaya ji dengi apko")
#     percentage = (paisa//len(questions)) * 100
#     print(f"Appka Status Ye raha : {percentage}%")
#     a = input()

# main()
# # import os

# # os.mkdir("python_workshop")
# student = [{"name":"xyz",
#             "marks":90},
#             {"name":"apoorav",
#             "mark":85},
#             {"name":"madhav",
#              "marks":95},
#              {"name":"vipin",
#               "marks":100}]
# list1 = [x for x in student if x["marks"]>90]
# list2=[]
# print(list1)
# print(list2)
# str1=["hrllo","hi","bye","welcome"]
# upper=list(map(str.upper,str1))
# print(upper)
# str1=[1,2,3,4,5,6,7,8,9,10]
# filter1=list(map(lambda x:x%2==0,str1))
# print(filter1)
# def is_prime(n):
#     """
#     count=0
#     for i in range(1,n+1):
#         if n%i == 0:
#             count +=1
#             if count < 3:
#                 return True
#                 else:
#                     return False
                    
#                     """
#     if n<=1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#           return False
#     return True
# str1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# print(len(str1))
# filter1=list(filter(is_prime,str1))
# double=list(map(lambda x: x**2,filter1))
# print(filter1)
# print(double)

#file handling

# file_name="radhika.txt"
# file = open(file_name,'w')
# file.write("hello radhika!")
# file.close()

# with open(file_name,'r')as file:
#     content= file.read()
#     print(content)
    
    
# data = [
#     ["hello","hi"],
#     ["python","java","css"]
# ]
# with open(file_name,'w')as file:
#     for i in data:
#      for j in range(len(i)):
#          file.write(f"item:{i[j]} |\n")
# import csv
# BASE_FILE="python.csv"
# # data = [
#     ['name','age','city'],
#     ['john','25','new york'],
#     ['alice','26','los angeles'],
#     ['bob','27','chicago']
# ]
# with open(BASE_FILE,'w',newline='')as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(data)
# with open(BASE_FILE,'r',newline='')as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)

# import csv
# BASE_FILE="cake.csv"
# data = [
#     ['apple', 'orange'],
#     ['dark choco','vanilla'],
#     ['black forest','butter scotch']
    
# ]
# with open(BASE_FILE,'w',newline='')as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(data)
# with open(BASE_FILE,'r',newline='')as csvfile:
#     reader=csv.reader(csvfile)
#     print("cake")
#     print("_"*6)
#     for row in reader:
#         for cake in row:
#             print(cake)
#     print("_"*6)
    
# import csv 
# BASE_FILE="user_data.csv"
# user_data=[]
# limit=int(input("how many record you want to insert:"))
# for _ in range(limit):
#     name=input("enter the name:")
#     marks=int(input("enter the marks:"))
#     user_data.append([name,marks])
# print(user_data)
# with open(BASE_FILE,'w')as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(user_data)

# fetched_details=[]
# with open(BASE_FILE,'r')as csvfile:
#     reader = csv.reader(csvfile)
#     for student in reader:
#         fetched_details.append(student)

# for i in fetched_details:
#     for j in range(0,1):
#         print(f"name:{i[j]}    and marks:{i[j+1]}")
# file_name ="students_data.txt"
# data=[{"name":"radhika",
#        "marks":90},
#        {"name":"kajal",
#         "marks":95},
#         {"name":"pooja",
#          "marks":98},
#          {"name":"mohit",
#           "marks":89},
#           {"name":"moksh",
#            "marks":96},
#            {"name":"aparna",
#             "marks":99}]
# with open(file_name,'w') as file:
#     for item in data:
#          file.write(f"name":{item["name"]} |and "marks":{item["marks"]})

# import csv
# BASE_FILE="cake.csv"
# data=[
#     ['orange','grapes','banana'],
#     ['apple','mango','pineapple'],
#     ['blueberry','strawberry','kiwi'],
#     ['cherry','watermelon','muskmelon']
# ]
# with open(BASE_FILE,'w',newline='')as csvfile:
#     writer=csv.writer(csvfile)
#     writer.writerows(data)
# with open(BASE_FILE,'r',newline='')as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)
# data = [
#     ['orange','pineapple'],
#     ['chocolate','strawberry']
# ]
# with open(BASE_FILE,'w',newline='')as csvfile:
#     writer=csv.writer(csvfile)
#     writer.writerows(data)
# with open(BASE_FILE,'r',newline='')as csvfile:
#     reader=csv.reader(csvfile)
#     print("cake")
#     print("_"*6)
#     for row in reader:
#         for cake in row:
#             print(cake+ " cake")
#     print("_"*6)

# import json
# BASE_FILE="anaconda.json"
# data = [
#     {"name":"pooja","age":78},
#     {"name":"radhika","age":99},
#     {"name":"shruti","age":100}
# ]
# def save(data):
#     with open(BASE_FILE,'w') as jsonfile:
#         json.dump(data,jsonfile,indent=4)

# def load():
#     with open(BASE_FILE,'r') as jsonfile:
#         data = json.load(jsonfile)
#         return data
# save(data)
# data2=load()
# for items in data2:
#     print(f"""name: {items["name"]}|age:{items["age"]}""")

# import sqlite3
# conn = sqlite3.connect("warehouse.db")
# c = conn.cursor()
# c.execute("""CREATE TABLE IF NOT EXISTS inventory
#           (id INT PRIMARY KEY,
#           name TEXT,
#           price REAL,
#           quantity INT)""")
# c.execute("""INSERT INTO inventory(id,name,price,quantity) VALUES(1,"lux",22.99,200)""")
# c.execute("""INSERT INTO inventory(id,name,price,quantity) VALUES(2,"margo",29.99,209)""")

# c.execute("""SELECT * FROM inventory""")
# data = c.fetchall()
# for item in data:
#     print(f"""product id : {item[0]} | product name : {item[1]} | product price : {item[2]} | product quantity : {item[3]} \n""")

# print("command successfully executed!")

# conn.commit()
# conn.close()

# import csv

# girls_serial_names = [
#     ['radhika','kajal','pooja'],
#     ['riya','shruti','priya'],
#     ['siya','janvi','soniya'],
#     ['kiara','katrina','tamanna']
# ]
# boys_cartoon_names = [
#     ['doraemon','nobita','sunio'],
#     ['jeon','shinchan','oggy'],
#     ['kainichi','amara','hatori'],
#     ['tom','jerry','mickey']
# ]
# def save_to_csv(data,filename):
     
#   with open(filename,'w',newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerows(data)
# def read_csv(filename):

#     data = []
#     with open(filename,'r') as csvfile:
#         reader = csv.reader(csvfile)
#     for row in reader:
#         data.append(row)
#     return data 
# def print_data(data,title):
#     print(title)
#     for i,row in enumerate(data):
#         print(f"row [i+1]:{row}")

# def main():
#     girls_filename = "girls_serial_names.csv"
#     boys_filename = "boys_cartoon_names.csv"
#     save_to_csv(girls_serial_names,girls_filename)
#     save_to_csv(boys_cartoon_names,boys_filename)
#     girls_data = read_csv(girls_filename)
#     boys_data = read_csv(boys_filename)
#     print_data(girls_data,"girl's serial names:")
#     print()
#     print_data(boys_data,"boy's cartoon names:")
#     if __name__ == "__main__":
#         main()
# import sqlite3
# conn = sqlite3.connect("School.db")
# c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS class
# (id INT,
# name TEXT,
# class INT,
# roll_number INT,
# address TEXT)""")

# class_data = []
# limit = int(input("Enter the number of records you want to enter : "))
# for _ in range(limit):
#     id = int(input("Enter the id of the student : "))
#     name = input("enter the name of the student : ")
#     Class = int(input("Enter the class of the student : "))
#     roll = int(input("Enter the Roll Number of the student : "))
#     addr = input("enter the Address Of Student : ")
#     class_data.append((id,name,Class,roll,addr))
 
# c.executemany("""INSERT INTO class VALUES(?,?,?,?,?)""",class_data)
# c.execute("""SELECT rowid,* FROM class""")
# data = c.fetchall()
# for items in data:
#     # print(items)
#     print(f"""Row Number : {items[0]} | student id : {items[1]} | student name : {items[2]} Ji | student class : {items[3]}th | student roll number : {items[4]} | student address : {items[5]}""")

# conn.commit()
# # conn.close()
# import sqlite3

# def create_table():
#     conn = sqlite3.connect("college.db")
#     c = conn.cursor()
#     c.execute("""CREATE TABLE IF NOT EXISTS students(
#     id INT,
#     name TEXT,
#     email TEXT)""")

#     conn.commit()
#     conn.close()

# def insert_value():
#     conn = sqlite3.connect("college.db")
#     c = conn.cursor()
#     students_data = []
#     record_limit = int(input("how many times to write : "))
#     for _ in range(record_limit):
#         id_ = int(input("enter the id : "))
#         name = input("enter the name of the student : ")
#         email = input("enter the email of the student : ")
#         students_data.append((id_,name,email))

#     c.executemany("""INSERT INTO students VALUES(?,?,?)""",students_data)

#     conn.commit()
#     conn.close()

# def show_all():
#     conn = sqlite3.connect("college.db")
#     c = conn.cursor()

#     c.execute("""SELECT * FROM students""")
#     data = c.fetchall()
#     for students in data:
#         # print(students)
#         print(f"""student id : {students[0]} | student name : {students[1]} | student email : {students[2]}""")

#     conn.commit()
#     conn.close()   
# def search_item():
#     conn = sqlite3.connect("college.db")
#     c = conn.cursor()

# # create_table()
# insert_value()
# show_all() 


# class dog:
#     def __init__(self):
#         self.name = "Kaju"
#         pass
#     def show_name(self):
#          print(f"The dog  name is {self.name}")

# Kaju = dog()
# Kaju.show_name()

# class employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age 
#         self.salary = salary
#     def show_details(self):
#         print(f"""Details of the employee:
#         Name : {self.name}
#         Age : {self.age}
#         Salary : {self.salary}""")

# name = employee("priya",24,20000)
# name.show_details()

# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def show_details(self):
#         print(f"Dog Name : {self.name}")
#         print(f"Dog age : {self.age}")
# class cat(Dog):
#     def __init__(self, name, age):
#         super().__init__(name, age)
        
# import sqlite3

# def create_table():
#     conn = sqlite3.connect("patient.db")
#     c = conn.cursor()
#     c.execute("""CREATE TABLE IF NOT EXISTS hospital
#     (Patient id INT,
#     Name TEXT,
#     Phone number INT,
#     Age INT,
#     Disease TEXT,
#     Attending doctor TEXT,
#     Ward number INT,
#     Days in hospital INT)""")

#     conn.commit()
#     conn.close()

# def insert_value():
#     conn = sqlite3.connect("patient.db")
#     c = conn.cursor()
#     # hospital_data = []
#     record_limit = int(input("how many times to write : "))
#     for _ in range(record_limit):
#         Patient_id = int(input("enter the Patient id : "))
#         Name = input("Enter the patient name : ")
#         Phone_number = int(input("Enter the phone number : "))
#         Age = int(input("Enter the age of patient : "))
#         Disease = input("Enter the disease : ")
#         Attending_doctor = input("Enter the doctor's name : ")
#         Ward_number = int(input("Enter the ward number : "))
#         Days_in_hospital = int(input("Enter the days in hospital of patient : "))

#         c.execute(""" INSERT INTO hospital(Patient_id,Name,Phone_number,Age,Disease,Attending_doctor,Ward_number,Days_in_hospital)
#          VALUES(?,?,?,?,?,?,?,?,?)""",(Patient_id,Name,Phone_number,Age,Disease,Attending_doctor,Ward_number,Days_in_hospital))

#     conn.commit()
#     conn.close()

# def show_all():
#     conn = sqlite3.connect("patient.db")
#     c = conn.cursor()

#     c.execute("""SELECT * FROM hospital""")
#     data = c.fetchall()
#     for hospital in data:
#         print(f"""Patient id : {hospital[0]} | Patient name : {hospital[1]} | Phone number : {hospital[2]} | Age : {hospital[3]} | Disease : {hospital[4]} | Attending doctor : {hospital[5]} | Ward number : {hospital[6]} | Days in hospital : {hospital[7]}""")

#         conn.commit()
#         conn.close()
# # create_table()
# insert_value()
# show_all()
# import sqlite3
# from datetime import date

# conn = sqlite3.connect("finance_tracker.db")
# c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS transactions
# (id INT,
# date TEXT,
# category TEXT,
# description TEXT,
# amount REAL)""")
# conn.commit()

# def add_transaction():
#     category = input("Enter category(income) : ")
#     description = input("Enter description : ")
#     amount = float(input("Enter amount : "))
#     today = date.today().strftime("%Y-%m-%d")

#     c.execute("""INSERT INTO transactions(date,category,description,amount) VALUES(?,?,?,?)""",(today,category,description,amount))
#     conn.commit()
#     print("Transaction added successfully! ")

# def view_transactions():
#     c.execute("SELECT * FROM transactions")
#     rows = c.fetchall()

#     for row in rows:
#         print(row)

# def view_balance():
#     c.execute("""SELECT SUM(amount)FROM transactions WHERE category = "income" """)
#     income = c.fetchone()[0] or 0 

#     c.execute("""SELECT SUM(amount)FROM transactions WHERE category = "expense" """)
#     expense = c.fetchone()[0] or 0

#     balance = income - expense 
#     print(f"Balance: {balance}")

# def delete_transaction():
#     id = int(input("Enter transaction id to delete : "))
#     c.execute("""DELETE FROM transactions WHERE id = ?""",(id))
#     conn.commit()
#     print("Transaction deleted successfully!")

# def main():
#     while True :
#         print("\n 1.Add Transaction ")
#         print("\n 2.View Transaction ")
#         print("\n 3.View Balance ")
#         print("\n 4.Delete Transaction ")
#         print("\n 5. Exit ")

#         choice = input("Enter your choice : ")

#         if choice == "1" :
#             add_transaction()
#         elif choice == "2" :
#             view_transactions()
#         elif choice == "3" :
#             view_balance()
#         elif choice == "4" :
#             delete_transaction()
#         elif choice == "5" :
#             break
#         else:
#             print("Invalid choice! ")
# main()

        
        
# import sys
# import json

# class LibraryManager:
#     def __init__(self):
#         self.filename = "library_books.txt"
#         self.books_list = []
#         try:
#             with open(self.filename,'r')as f:
#                 self.books_list = json.load(f)
#         except (FileNotFoundError,json.JSONDcodeError):
#             self.books_list = []
#     def save_books(self):
#         with open(self.filename,'w')as f:
#             json.dump(self.book_list,f,indent = 4)

#     def add_books(self):
#          while True:
#             try:
#                  name = input("Enter the name of the book : ")
#                  author = input("Enter the name of the author of the book: ")
#                  genre = input("Enter the name of genre/category of the book: ")
#                  price = float("Enter the price of book: ")
#                  self.book_list.append("name" : name , "author" : author , "genre" : genre , "price" : price)
#                  self.save_books()
#                  print(f"the book '{name}' added to the library records!")
#                  another_book = input("Do you want to add another book (y/n): ").lower()
#                  if  another_book = not in ("y","yes"):
#                    break
#             except ValueError:
#                 print("Invalid price format.please enter a valid nummerical")              


#     def remove_books(self):
#         try:
#             num = int(input("Enter the number : "))
#             if num>len(self.books_list):
#                 raise ValueError(f"Invalid number of books. There are only")
#             for _ in range(num):
#                 name = input("Enter the name of the book to remove:")
#                 for book in self.books_list:
#                     if book["name"].lower() == name.lower():
#                         self.books_list.removed(book)
#                         self.save_books()
#                         print(f"The book '{name}' is removed successfully!")
#                         break
#                     else:
#                         print(f"The book '{name}' not found in the library")
#                         break
#                     except ValueError as e:
#                         print(e)
# def display_books(self):
#     if self.books_list:
#         print("| Book-Name | Author | Genre | Price |")
#         for book in self.books_list:
#             print(f'{book["name"]} | {book["genre"]} | {book["price"]:}')
#         else:
#             print(f"No books found by {author}.")

# def author_collection(self):
#     author = input("Enter the author's name :")
#     author_books = [book for book in self.books_list if book["author"].lower]
#     if author_books:
#         print(f"books by {author}:")
#         for book in author_books:
#             print(f'{book["name"]} | {book["genre"]} | {book["price"]}')
#     else:
#         print(f"No book found by {author}.")

# def genre_collection(self):
#     genre = input("enter the genre : ")
#     genre_books = [book for book in self.books_list if book["genre"].lower()]
#     if genre_books:
#         print(f"books n the {genre} genre: ")

# def 


