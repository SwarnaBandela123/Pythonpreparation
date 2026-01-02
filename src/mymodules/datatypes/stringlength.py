string = input("Enter the String :")

String_length=len(string)
print("Length of the string using len - Built in function: ", String_length)

count=0
for char in string:
    count+=1
print("Length of the string using for loop: ", count)

countchar=0
while string[countchar:countchar+1]:
    countchar+=1
print("Length of the string using while loop: ", countchar)

length = sum(1 for _ in string)
print("Length of the string using sum method:", length)
