'''
#calculator
num1 = float(input("Enter the first number:"))
operation = input("Enter the operation (+, -, *, /):")
num2 = float(input("Enter the second number:"))
if operation == "+":
    result = num1 + num2        
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
print("Result:", result)  

#odd/even
No = int(input("Enter a number: "))
if (No % 2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")

one = float(input("Enter your 1'st number: "))
two = float(input("Enter your 2'nd number: "))
three = float(input("Enter your 3'rd number: "))
if(one>two and one>three):
    print("The greatest number is:", one)
if(two>one and two>three):
    print("The greatest number is:", two) 
if(three>one and three>two):
    print("The greatest number is:", three)     
else:
    print("2 or more no. are equal.")

#palidrome
list = []
list.append(input("Enter 1st element: "))
list.append(input("Enter 2nd element: "))        
list.append(input("Enter 3rd element: "))
copylist1 = list.copy()
copylist1.reverse()
if list == copylist1:
    print("It is a palindrome")
else:
    print("It is not a palindrome") 
    
dic = {
    "table" : ["A peice of furniture", "list of facts and figures"],
    "cat" : "a small animal",
}

dic = {}
dic["Physic"] = [input("Enter your marks in Physic: ")]
dic["Chemistry"] = [input("Enter your marks in Chemistry: ")]
dic["Maths"] = [input("Enter your marks in Maths: ")]       
dic["english"] = [input("Enter your marks in English: ")]
print(dic)

i = 0
while i <= 10:
    print(int("n") * i)
    i += 1

i = 1
while i <= 10: 
    print(i*i)
    i += 1

heros = [ "ironman", "supeman", "thor", "hulk", "captain america"]
i = 0
while i < len(heros):
    print(heros[i])
    i += 1

from operator import index


x  =int(input("Enter the value of x: "))
i = 0
slist = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100 )
while i < len(slist):
    if(slist[i] == x):
        print("The no. is found at index", i)
    i += 1
else:
    print("No. not found")

x = int(input("Enter the value of x: "))
olist = (1,4,9,16,25,36,49,68,81,100)
i = 0
while i < len(olist):
   if(olist[i] == x):
        print("the no. is found at index: ", (i + 2))
        break
   i += 1
else:
    print("The no. is missing in the list.")

i = 1
while i<= 10:
    print(i)
    if i == 9:
        break
    i += 1
print("Loop Ended")
  
list = [1,4,9,16,25,36,49,64,81,100]
for no in list:
    print(no)

n = int(input("Enter the value of n: "))
for i in range(0,11):
    print(n * i)

n = int(input("Enter the value of n: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("The sum of first", n, "natural numbers is:", sum)

n = int(input("Enter the value of n: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print ("The factorial of", n, "is:", fact)

def print_length(list)  :
    print("The length of the list is:", len(list))

my_list = [1, 2, 3, 4, 5]
print_length(my_list)   

def elements(list):
    for elements in list:
        print(elements, end=" ")

my_list = [1, 2, 3, 4, 5]
elements(my_list)

def fact(n):
    fact = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n+1):
            fact *= i  
        print(fact)

  
fact(2)

def convert(USD,INR=82.5):
    con = USD * INR
    print(USD, "USD is equal to", con, "INR")

convert(150)

def o_e(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("ODD")

o_e(5)

def sum(n):
    if n == 0:
        return 0
    else:
        return  n + sum(n-1)

print(sum(5))

def el(list):
    print(list, end="")

f = ("hi", 'my', 'name', 'is', 'avika')
el(f)

f = open("try.txt", "a")

f.write("/ni love myself")
f.close()

class Students:
    def __init__(self, name, english, hindi, maths):
        self.name = name
        self.english = int(english)
        self.hindi = int(hindi)
        self.maths = int(maths)
    def avg(self):
        sum = self.english + self.hindi + self.maths
        avg = sum / 3
        print("The average marks of", self.name, "is:", avg)

s1 = Students("Avika", 96, 97, 98)
s1.avg()

class account:
    def __init__(self,balance,account,):
        self.balance = balance
        self.account = account
    def deposit(self,amount):
        self.balance += amount
        print("The new balance in the account is: ", self.balance)
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("The new balance in the account is: ", self.balance)

a1 = account(1000, 123456789)
a1.deposit(500)
a1.withdraw(200)

class circle:
    def __init__(self,radius):
        self.radius = radius
    def __area__(self):
        area = 3.14 * self.radius * self.radius
        print("The area of the circle is:", area)
    def __perimeter__(self):
        perimeter = 2 * 3.14 * self.radius
        print("The perimeter of the circle is:", perimeter)

ci = circle(5)
print(ci.__area__(), ci.__perimeter__())

class employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary        

    def showDetails(self):
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)

class enginer(employee):
    def __init__(self,name,age ):
        self.name = name
        self.age = age  
        super().__init__("enginer", "development", 50000)

e1 = enginer("Avika", 17)
e1.showDetails()
'''
class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, other):
        if self.price > other.price:
            print(self.item, "is more expensive than", other.item)  
        else:
            print(other.item, "is more expensive than", self.item)

o1 = order("laptop", 50000)
o2 = order("phone", 30000)
o2 > o1