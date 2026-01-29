#Basic program
x=lambda a,b:a+b
print(x(1,2))

x = lambda a : a + 10
print(x(5))

#Multiple arguments
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Lamda Function within function
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

#Using Lambda with map()
number=[1,2,3,4,5,6]
evennum=list(map(lambda x: x % 2==0, number))
print(evennum)

#Lamda function using filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#Using sorting
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1],reverse=False)
print(sorted_students)