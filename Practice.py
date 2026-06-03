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
'''
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