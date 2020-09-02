"""
Program to provide users with how old they are in months,days,hours, minutes, and seconds
    1. Ask user for input of their message
    2. Provide how old they are in months, days, hours, minutes, seconds
"""

print('Welcome to the age program!')
age = input('Please enter how old you are:\n')
convertedage = int(age)
print('You are',convertedage * 12, 'months old')
print('You are',convertedage * 365,' days old')
print('You are',convertedage * 365 * 60, 'hours old')
print('You are',convertedage * 365 * 60 * 60, 'minutes old')
print('You are',convertedage * 365 * 60 * 60* 60, 'seconds old')
