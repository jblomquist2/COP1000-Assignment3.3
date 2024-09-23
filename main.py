validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

year =
month =
day =

if int(year) <= MIN_YEAR: 
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: 
    validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: 
    validDate = False


if validDate:
    print(f"{month}/{day}/{year} is a valid date.")
else:
    print(f"{month}/{day}/{year} is an invalid date. ")