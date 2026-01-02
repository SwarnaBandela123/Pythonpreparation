numbers = [10, 20, 30, 40, 50]

total = sum(numbers)
print("Sum of numbers using sum method:", total)

sumofall=0
for num in numbers:
    sumofall+=num
print("Sum of numbers using for loop:", sumofall)

whiletotal=0
i=0
while i < len(numbers):
    whiletotal+=whiletotal+numbers[i]
    i+=1
print("Sum of numbers using while loop:", sumofall)

total1 = sum([num for num in numbers])
print("Sum of numbers using sum:", total1)
