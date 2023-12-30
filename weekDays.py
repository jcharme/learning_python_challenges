"""
Counts how many of the given weekday there are in a month 
Ex. How many mondays are there in Dec 2024?
"""
import calendar

def count_days(year, month, whichday):
    count = 0
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        if week[whichday] != 0:
            count += 1
    return count

# This is how your code will be called.
# You can edit this code to try different testing cases.
testyear = 2025
testmonth = 12
testday = 0
result = count_days(testyear, testmonth, testday)
print(result)