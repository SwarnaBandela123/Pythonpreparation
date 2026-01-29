#Basic def function
def def_fun():
    print("Learning def functions")
def_fun() # Calling a function

#Print even odd
def evenodd(x):
    if x % 2 == 0:
        print('Even :',x)
    else:
        print('Odd :',x)
evenodd(3)
evenodd(4)

#Multiple arguments - Addition
def add(a,b):
    return a+b
print(add(a=1,b=2))

def add1(a,b):
    result=a+b
    print(result)
add1(a=1,b=2)
add1(10,20)

#Parameters and Argumenrts
def my_function(name): # name is a parameter
  print("Hello", name)
my_function("Emil") # "Emil" is an argument

#Number of arguments
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")

#Deault arguments
def my_function(name = "friend"):
  print("Hello", name)
my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#Keyword argument
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
my_function(animal = "dog", name = "Buddy")

#Positional arguments
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

print("Case-2:")
nameAge(27, "Suraj")

#Using args with realtime arguments
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")