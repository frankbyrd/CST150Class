"""
A fact file about circles
Ask the user to enter an integer radius value
create a variable for pi and give it the value 3.14159
    Next calculates
        Circumference
        Area
    Print this to the screen in a message to the user
"""
print('Hello, Welcome to my circle fact program.')
radius = input('Please enter a radius value: ')
conradius = float(radius)
pi = 3.14159
print('The Circumference of your circle is:', conradius * 2 * pi)
print('The area of your circle is:', pi*conradius**2) #multiply pi times radious to 2nd power
