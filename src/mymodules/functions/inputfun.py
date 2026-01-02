
'Basic input'
name=input("Enter your name: ")
print('My name is '+name)

"Numeric input"
salary=input("Enter your salary: ")
bonus=input("Enter your bonus: ")
monthly_salary=salary+bonus
print('Employee monthly salary:', monthly_salary)
'In python it always take input in a string formate even if we enter numeric also'

'Using Typecasting - we can give the integer and flot values in the input'
"integer datatype"
salary1=int(input("Enter your salary: "))
bonus1=int(input("Enter your bonus: "))
Swarna_salary=salary1+bonus1
print('Employee Swarna monthly salary:', Swarna_salary)

"flot datatype"
salary2=int(input("Enter your salary: "))
bonus2=int(input("Enter your bonus: "))
thanusha_salary=salary2+bonus2
print('Employee Thanusha monthly salary:', thanusha_salary)

'Taking Multiple Inputs'
x, y = input("Enter two numbers separated by space: ").split()
print("First number:", x)
print("Second number:", y)

'Taking Lists as Input'
listvalue=list(input("Enter your list: ").splitlines())
print("list values:", listvalue)

'Taking Input Using a Loop'
num=int(input("Enter number of elements: "))
a=[]
for i in range(num):
    element=input(f"Enter element {i+1}: ")
    a.append(element)
    print(a)


