
a = 5
b = 3
sum = a + b
print(sum)
print(a**b)
print(b**a)

num = 10
num **= 10
print("num-", num)

print(a >= b)
print(a != b)

print( not (a > b) or a != b)

c = str(15)
d = 20.0

print( type(c))
print( type(d))

name = input("Your name:")
print("WELCOME!", name)

val = int(input("Enter a number: "))
print(type(val), val)
#)(*&^%$#@!!@#$%^&*()_+~!@#$%^&*()_+~!@#$%^&*()_+)
fruits = ["apple", "banana", "mango"]
print(fruits)

print(fruits[0])
print(fruits[1])

fruit = ["apple", "banana"]
fruit.append("mango")
print(fruit)

f = ["apple", "banana", "mango"]
f.remove("banana")
print(f)
str1 = "i My name is Avika Bansal.\nI am 17 years old"
#print(str1)
str2 = "My name is Avika Bansal.\tI am 17 years old"
print(str2)
print(str1 + str2)
print (len(str1), len(str2))
print(str1[0:10])
print(str2[-24:-1])
print(str1.endswith("hu"))
print(str1.capitalize())
print(str1.replace("Avika", "Avika Bansal"))
print(str1.find("Avika"))
print(str1.count("a"))

name = input("Write your first name:")
print("Your name is:", name)
print("length of your first name is:", len(name))
str = "avika.Bansal.gh.dhgc.hgwdsx.bgwcf"
print(str.count("."))

age = int(input("Enter your CURRENT AGE: "))
if(age>=18):
    print("You are eligible to vote")
elif(age<18 and age>=0):
    print("You are not eligible to vote")

marks = float(input("marks of the student: "))
if(marks >= 90 and marks <= 100):
    print("Grade A")
elif(marks >= 80 and marks < 90):
    print("Grade B")
elif (marks >= 70 and marks < 80):
    print("Grade C")
elif (marks >= 60 and marks < 70):
    print("Grade D")

student = ["karan", 17, 90.5, "A"]
print(student[0])
student[2] = "avika"
print(student)

list = ["avika", "karan", "yadav", "bansal"]
list.append(5)
print(list)
print(list.sort())
list.reverse()
print(list)
print(list.insert(1, "avika"))

Movies = []
Movies.append(input("Enter your 1st favourite movie: "))
Movies.append(input("Enter your 2nd favourite movie: "))
Movies.append(input("Enter your 3rd favourite movie: "))
print(Movies)

dict = {
    "name": "avika",
    "age": 17,
    "marks": 90.5,
    "grade": "A"    
}
print(dict["name"])
print(dict["age"])
print(dict["marks"])
print(dict["grade"])

dict["surname"] = "Bansal"
print(dict)

student = {
    "name": "Avika",
    "Subjects": {
        "Maths": 80,
        "Science": 75,
        "English": 95
    }
}
print(student["Subjects"]["English"])
print(list(student.items()))
print(student.get("name"))

numbers = {1, 2, 9, 9, "hello", "world"}
set1 = { 1,3,4,8,9}
print(numbers)
print(type(numbers))  
print(numbers.pop())
print(numbers.pop())
print(set1.union(numbers))
print(set1.intersection(numbers))

count = 1
while count <= 5: 
   print("hello")
   count += 1

i = 8
while i >= 1:
    print(i)
    i -= 1
print("Loop Ended")

i = 0
while i >= -16:
    if(i == 9): 
        i -= 1
        continue
    print(i)
    i -= 1

string = "Avika Bansal" 
for char in string:
    print(char)
    if(char == 'p'):
        break
else:
    print("Loop Ended")

seq = range(10)
for i in seq:
    print(i+1)

for i in range(32,64,8):
    print(i)

def calc_sum(a,b):
    sum = a+ b
    print(sum)

calc_sum(5,8)    
calc_sum(10,20)

def avg(a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)

avg(5,9,10)
avg(10,20,30)

def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)
    print("END")

show(5)

def fact(n):
    if n == 0:
        return 1        
    return fact(n-1) * n

print(fact(6))

class Student:
    name = "Avika Bansal"

s1 = Student()
print(s1.name)

class student:
    def __init__(self, name, age):
        self.name = print(name)
        self.age = print(age)
        print("Student created successfully")

    def welcome(self):
         print("Welcome", self.name)

s1 = student("Avika Bansal", 17)
s1.welcome()

class account:
    def __init__(self, account, pas):
        self.account = account
        self.__pas = pas

s1 = account("Avika", "1234")
print(s1.account)

class car:
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car stopped")
    def __init__(self, type):
        self.type = type

class Toyota(car):
    def __init__(self, brand):
        self.brand = brand

class Honda(Toyota):
    def __init__(self, type):
        self.type = type
        super().__init__("car")
 
 class student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math