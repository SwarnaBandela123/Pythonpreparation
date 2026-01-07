count = 1
while count <= 3:
    print("Count is:", count)
    count += 1

#Using Else block
count = 1
while count < 3:
    print("Count:", count)
    count += 1
else:
    print("Loop finished")

#Calculate factorial of a number using a while loop:
print('Calculate factorial of a number using a while loop:')
num = 5
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(factorial)

#Find the first occurrence of a number in a list using a while loop:
print('Find the first occurrence of a number in a list using a while loop:')
my_list = [3, 8, 2, 7, 4]
target = 7
index = 0
while index < len(my_list):
    if my_list[index] == target:
        break
    index += 1
else:
    index = -1
print(index)

#Calculate the sum of numbers from 1 to 100 using a while loop:
print('Calculate the sum of numbers from 1 to 100 using a while loop:')
num = 1
sum_numbers = 0
while num <= 100:
    sum_numbers += num
    num += 1
print(sum_numbers)

#Print the Fibonacci sequence up to the 10th term using a while loop:
print('Print the Fibonacci sequence up to the 10th term using a while loop:')
a, b = 0, 1
count = 0
while count < 10:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

#Print numbers in a list until a negative number is encountered using a while loop:
print()
print('Print numbers in a list until a negative number is encountered using a while loop:')
my_list = [1, 4, 6, 8, 10, -3, 5, 7]
index = 0
while my_list[index] >= 0:
    print(my_list[index])
    index += 1








