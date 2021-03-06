# The valid_month() function takes a string
# and verifies whether the data a user enters
# is a valid month. If the passed in parameter
# 'month' is not a valid month, return None. 
# If 'month' is a valid month, then return 
# the name of the month with the first letter 
# capitalized.

months = ['January', '1', '01',
          'February', '2', '02',
          'March', '3', '03',
          'April', '4', '04',
          'May', '5', '05',
          'June', '6', '06',
          'July', '7', '07',
          'August', '8', '08',
          'September', '9', '09',
          'October', '10', '10',
          'November', '11', '11',
          'December', '12']
          
def valid_month(month):
    if month:
        cap_month = month.capitalize()
        if cap_month in months:
            return cap_month

# print valid_month("january") => "January"    
# print valid_month("January") => "January"
# print valid_month("foo") => None
# print valid_month("") => None



# The valid_day() function takes as 
# input a String, and returns either a valid 
# Int or None. If the passed in String is 
# not a valid day, return None. 
# If it is a valid day, then return 
# the day as an Int, not a String. Don't 
# worry about months of different length. 
# Assume a day is valid if it is a number 
# between 1 and 31.

def valid_day(day):
    if day.isdigit():
        day = int(day)
        if day > 0 and day < 32:
            return day

# print valid_day('0') => None    
# print valid_day('1') => 1
# print valid_day('15') => 15
# print valid_day('500') => None



# The valid_year() function verifies 
# whether the string a user enters is a valid 
# year. If the passed in parameter 'year' 
# is not a valid year, return None. 
# If 'year' is a valid year, then return 
# the year as a number. Assume a year 
# is valid if it is a number between 1900 and 
# 2020.
#

def valid_year(year):
    if year.isdigit():
        year = int(year)
        if year >= 1900 and year <= 2020:
            return year

# print valid_year('0') => None    
# print valid_year('-11') => None
# print valid_year('1950') => 1950
# print valid_year('2000') => 2000
