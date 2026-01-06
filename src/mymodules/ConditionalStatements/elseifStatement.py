#Tax calculation based on the vechile price

Bike_price=int(input('Enter your bike price: '))

if Bike_price>100000:
    Tax=Bike_price*15/100
    print('Tax(15%) based on the Bike_price', Tax)
elif Bike_price>=50000 and Bike_price<=100000:
    Tax = Bike_price * 10 / 100
    print('Tax(10%) based on the Bike_price', Tax)
elif Bike_price<50000:
    Tax = Bike_price * 5 / 100
    print('Tax(5%) based on the Bike_price', Tax)

##Find leap year
year=int(input('Enter your year: '))
if year%400==0 or (year%4==0 and year%100!=0):
    print('Leap YEAR YES')
else:
    print('Not Leap YEAR YES')


#Print a day by giving input like 1 to 7 example: 1=Sunday, 2=Monday, 3=Tuesday, 4=Wednusday, 5=Thursday, 6=Friday, 7=Saturday
day_num=int(input('Enter your day number: '))
if day_num==1:
    print('Sunday')
elif day_num==2:
    print('Monday')
elif day_num==3:
    print('Tuesday')
elif day_num==4:
    print('Wednesday')
elif day_num==5:
    print('Thursday')
elif day_num==6:
    print('Friday')
elif day_num==7:
    print('Saturday')
else:
    print('Please enter a valid day number (1 to 7)')


