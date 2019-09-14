'''Conditional Statements

Three conditional statements
 1- if
 2- elif
 3- else

allows our code to do certain things depending on certain conditions
'''

# last lesson
#a = 1
#b = 2

#c = a + b

# print(a)
# print(b)
# print(c)

# conditional statements
grade = -100

if grade > 100 or grade < 0:
    print('not a valid grade')
elif grade >= 90:
    print('You got an A! Awesome!')
elif grade >= 80:
    print('You got a B! Good job')
elif grade >= 70:
    print('You got a C! Try harder')
else:
    print('You failed!')

# operators <, > , <= , >= , == , !=

game_over = True
if game_over:
    print('You lost')

# nested if statements
grade = 87

if grade > 90:
    print('You got an A')
elif grade > 80:
    if grade < 83:
        print('You got a B-')
    elif grade < 86:
        print('You got a B')
    else:
        print('You got a B+')
else:
    print('You got a C or worse')

# and, or , (), not
if not(False and (False or True)):
    print('passed')

# challenge problem: write a set of conditional statements to find out if a number is a special number. Special number is defined less than 100 or greater than or equal to 300, perfectly divisible to 3, 7, or both.

# print out 'Divisible by both' if special number divisible by both 3 & 7
# print out 'Divisible by 3' if special number divisible by 3, but not 7
# print out 'Divisible by 3' if special number divisible by 7, but not 3
# print out 'Not a special number otherwise'

number = 300

if (number < 100 or number >= 300) and (number % 7 == 0 or number % 3 == 0):
    if (number % 7 == 0 and number % 3 == 0):
        print('This is a special number that is divisible by both')
    elif number % 3 == 0:
        print('Special number that is divisible by 3, but not 7')
    else:
        print('Special number that is divisble by 7, but not 3')
else:
    print('Not a special number')
