age=int(input('Enter Age :'))
if age>18:
    print('Person age is greater than 18')


##Find leap year
year=int(input('Enter your year: '))
if year%400==0 or (year%4==0 and year%100!=0):
    print('Leap YEAR YES')
else:
    print('Not Leap YEAR YES')