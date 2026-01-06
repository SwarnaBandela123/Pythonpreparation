# To check whether the person is eligible for voting based on age
age=int(input('Enter your age: '))
if age>=18:
    print('Person is eligible for voting as he/she age is >= 18 :', age)
else:
    print('Person is not eligible for voting as he/she age is < 18 :', age)


#Check whether the user entered number is even or odd
num=int(input('Enter your number: '))
if num%2==0:
    print('user entered value is even: ', num)
else:
    print('user entered value is odd :', num)

#Check whether the given number is divisible by 7 or not
if num%7==0:
    print('user entered value is divisible by 7 :', num)
else:
    print('user entered value is not divisible by 7 :', num)

#Print "Hello" if the entered num is multiple of 5, otherwise "Bye"
if num%5==0:
    print('Hello')
else:
    print('Bye')


#Last digit of a given number is dividible by 3
number=int(input('Enter your number: '))
divisible_num=number%10
if divisible_num%3==0:
    print('Last digit of a given number is dividible by 3 :', divisible_num)
else:
    print('Last digit of a given number is not dividible by 3 :', divisible_num)

#Segregate the students grade based on marks
marks=int(input('Enter your marks: '))
if marks>90:
    print('Your marks is greater than 90 and student grade is A')
if marks>80 and marks<=90:
    print('Your marks between 80 & 90 and student grade is B')
if marks>=60 and marks<=80:
    print('Your marks between 60 & 80 and student grade is C')
if marks<60:
    print('Your marks below 60 and student grade is D')


#Check whether the number entered is three digit number or not
Num=number.bit_length()
if Num==3:
    print('Number input is 3 digit number')
else:
    print('Number input is not 3 digit number')