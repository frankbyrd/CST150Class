
"""
An interactive program to perform some math operations
Authors: Kyle Case, Lon Hawk, Frank W Byrd
"""

print('Are you ready to play a game? (y/n) ')
answer = input() # assigning the variable answer to the information the user enters.
if answer == "y": # Checking to see if the user wants to play, if Y then continue, if N then end program
    favnum = input('Please enter your favorite number: ')
    connum = int(favnum)
    print('2 times your number is: ',connum * 2)
    print('Adding 5 to your number: ',connum * 2 + 5)
    print('Now multiply by 50: ',(connum * 2 + 5) * 50)
    print('Now add 1769: ',(connum * 2 + 5) * 50 + 1769)
    yearborn = input('What year were you born?\n')
    cake = input('Have you had your birthday yet? (y/n)')
    print(cake)
    if cake == 'n':
        print('Subtract the year you were born: ', (connum * 2 + 5) * 50 + 1769 - int(yearborn))
        print('The answer begins with your favorite number and ends with your age: ' ,(connum * 2 + 5) * 50 + 1769-int(yearborn))
    else:
        print('Subtract the year you were born: ', (connum * 2 + 5) * 50 + 1769 - int(yearborn) +1 )
        print('The answer begins with your favorite number and ends with your age: ' ,(connum * 2 + 5) * 50 + 1769-int(yearborn) +1)
else:
    print('Have a nice day!')
