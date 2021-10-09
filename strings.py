"""
    String in python are surrounded by either single or double quoatation mark.
    '' ""
"""

# name = 'Mukund'
# age = '28'
# isActive = 'True'

stringOne = "salahuddin"
stringTwo = "Developer"

# print(stringOne+' '+stringTwo)

x = f'{stringOne} {stringTwo}'
# print(x)

print('my name is {name} I am {x}'.format(name='Mukund', x=stringTwo))

print(stringOne)
print(stringOne.capitalize())
print(stringOne.upper())

