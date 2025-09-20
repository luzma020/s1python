year = int(input("Enter a year: "))

# Leap year conditions:
# 1. Year is divisible by 4 and not divisible by 100
# 2. Or year is divisible by 400

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")