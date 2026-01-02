# Check if a number lies between 10 and 50
num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
    print("Number is between 10 and 50")
elif num < 0 or num > 100:
    print("Number is outside the range")
elif not (num >= 18):
    print("You are not eligible to vote")
else:
    print("You are eligible to vote")