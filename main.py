# Constants
validDate = True
MIN_DAY = 1
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12

# User Inputs
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
year = int(input("Enter the year: "))

# If Statements
if month in (4, 6, 9, 11):
    maxDay = 30
else:
    maxDay = 31

if int(year) <= MIN_YEAR: 
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: 
    validDate = False
elif int(day) < MIN_DAY or int(day) > maxDay: 
    validDate = False

if validDate == True:
    print(f"{month}/{day}/{year} is a valid date")
else:
    print(f"{month}/{day}/{year} is an invalid date")