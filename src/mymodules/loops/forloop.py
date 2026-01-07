from ftplib import print_line

for i in range(5):
    print('Count :', i)

#Using Index to Iterate Through a Sequence in Python:
print('Using Index to Iterate Through a Sequence in Python :')
names=["Swarna","Thanusha","Shivani","Nirmala","Navanitha"]
for i in range(len(names)):
    print(f'Index :{i} , Names {names[i]}')

for name in names:
    print(f'Names :{name}')

#Using else Statement with a for Loop in Python
print('Using else Statement with a for Loop in Python :')
for i in range(3):
    print(i)
else:
    print('Loop completed')

#Loop ends with break statement:
print('Loop ends with break statement :')
for i in range(3):
    print(i)
    if i==1:
        break
else:
    print('Loop completed')

#Print numbers from 1 to 10 using a for loop:
print('Print numbers from 1 to 10 using a for loop :')
for num in range(1,11):
    print(num)

#Calculate the sum of numbers from 1 to 10 using a for loop:
print('Calculate the sum of numbers from 1 to 10 using a for loop:')
sum = 0
for num in range(1,11):
    sum+=num
print('Sum of numbers from 1 to 10 :',sum)

#Print elements of a list
print('Print elements of a list :')
Fruits=["Apple","Banana", "Carrot", "Dragon"]
for fruit in Fruits:
    print(fruit)

#Calculate the product of elements in a list using a for loop:
print('Calculate the product of elements in a list using a for loop:')
number=[1,10,5,4,12]
product = 1
for num in number:
    product*=num
print('Product of elements in a list(number):',product)

#Print even numbers from 1 to 10 using a for loop:
print('Print even numbers from 1 to 10 using a for loop :')
for num in range(1,11):
    if num%2==0:
        print('Even number :',num)
for num in range(2, 11, 3):
    print(num)

#Print numbers in reverse from 10 to 1 using a for loop:
print('Print numbers in reverse from 10 to 1 using a for loop:')
for num in range(10,0,-1):
    print(num)

#Print characters of a string using a for loop:
print('Print characters of a string using a for loop:')
string='Learnings'
for char in string:
    print(char)

#Find the largest number in a list using a for loop:
print('Find the first and second largest number in a list using a for loop:')
list1=[5, 7, 9, 8]
largest=0
for num in list1:
    if num>largest:
        largest=num
print('First largest value from a list :',largest)

#Find the Second largest number in a list using a for loop:
largest1=0
second_largest=0
for num in list1:
    if num>largest1:
        second_largest = largest1
        largest1=num
    elif num>second_largest and num!=largest1:
        second_largest=num
print('First second-largest value from a list :',second_largest)

#ind the average of numbers in a list using a for loop:
print('ind the average of numbers in a list using a for loop:')
Sum=0
list_length=len(list1)
for num in list1:
    Sum+=num
list_average=Sum/list_length
print('The average of numbers in a list :',list_average)

#Print all uppercase letters in a string using a for loop:
print('Print all uppercase letters in a string using a for loop:')
string='Learnings Python'
for A in string:
    if A.isupper():
        print(A)

#Count the number of vowels in a string using a for loop:
print('Count the number of vowels in a string using a for loop:')
my_string = "Hello World"
vowels = "AEIOUaeiou"
count = 0
for char in my_string:
    if char in vowels:
        count += 1
print(count)

#Print Right half pyramid

for i in range(1, 4):
    for j in range(i):
        print('*', end=' ')
    print()

