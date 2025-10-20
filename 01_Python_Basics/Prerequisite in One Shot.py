print("Hello World")

#Printing the average:
# this program finds the
# average attendance of
# monday and tuesday

"""this program finds the
average attendance of
monday and tuesday"""

monday = 87 # attendance of monday
tuesday = 64 # attendance of tuesday

avg = (monday+tuesday)/2

print(avg)

#Printing the name
name_10 = "abhinav"
age1 = 100

_address = "bangalore"
address = "bangalore"

name = "Abhinav"
Name = "Awasthi"

print(name)
print(Name)

# Arithmetic Operations
print(34+324)
print(34-324)
print(34*324)
print(34/3)
print(34//3)
print(34%3)
print(2**3)

# Assignment Operators
a = 5
a+=2
a*=3

print(a)

# Data Types in Python
age = 100 # integer
height = 12.43# float
c = 2+3j# complex number

print(age,type(age))#   print the value and type of age
print(height,type(height))# print the value and type of height
print(c,type(c))# print the value and type of c


# Strings in Python
s1 = 'a'
s2 = "abhinav"
s3 = "my name is abhinav"

print(s1,type(s1))
print(s2,type(s2))
print(s3,type(s3))


# Boolean in Python
isMarried = False
isGraduated = True

print(isMarried,type(isMarried))
print(isGraduated,type(isGraduated))

# None Type in Python
name = None

print(name,type(name))

s = "24231"
print(int(s))


# Input in Python
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(first_name,last_name)

# Taking multiple inputs in one line
age = int(input())
height = float(input())

print(age,height)

# Formatting the output in Python
full_name = "abhinav awasthi"
age = 100
address = "bangalore"

print(full_name,end = "&&")
print(age)
print(address)

print(full_name,age,address,sep="-")

#take input of age and on the basis of age print eligible or not eligible for driving license
age = int(input())

if(age>=18):
  test = input()
  if test=="PASS":
    print("Eligible for Driving License")
  else:
    print("Not Eligible for Driving License")
else:
  print("Not Eligible for Driving License")


# Take input of marks and print the grade according to the following criteria
marks = int(input())

# >=90 Excellent
# 70-90 Good
# 40-70 Fair
# <40 Bad

if marks>=90:
  print("Excellent")
elif marks>=70:
  print("Good")
elif marks>=40:
  print("Fair")
else:
  print("Bad")

# Take input of temperature and print the following
temp = int(input())

# 25-50->  Hot
# 10-24-> Cold
# <10 -> Extremely Cold

if 25<=temp<=50:
  print("Hot")
elif 10<=temp<=24:
  print("Cold")
elif temp<10:
  print("Extremely Cold")

#   Logical Operators
a = True
# Ternary Operator

age = int(input())

result = "Eligible" if age>=18 else "Not Eligible"

print(result)

# Loops in Python
i = 0

while i<5:
  print(i,end=" ")
  i+=1

# For Loop
list1 = [3,3,5,2,1]

for i in list1:
  print(i,end=" ")

# Print numbers from 1 to 10
for i in range(1,11):
  print(i,end=" ")
print()

for i in range(5,11):
  print(i,end=" ")
print()

for i in range(1,11,2):
  print(i,end=" ")
print()

for i in range(20,0,-1):
  print(i,end=" ")
print()

for i in range(20,0,-3):
  print(i,end=" ")
print()

# Functions in Python
def printName(name):
  print(name)

printName("Arpreet Mahala")

# Function to add two numbers
def addTwoNumbers(a,b):
  sum = a+b
  return sum

ans = addTwoNumbers(4,7)
print(ans)

# Print digits of a number in reverse order
n = 5183

while n>0:
  r = n%10
  print(r,end=" ")
  n//=10


  n = 5183

# Print sum of digits of a number
sum = 0

while n>0:
  r = n%10
  sum+=r
  n//=10

print(sum)