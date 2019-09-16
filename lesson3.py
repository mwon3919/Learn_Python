'''Functions

Functions allow you to simplify your code that allows you to break it into small reusable components'''


def spam():
    # when writing a function you first start with def than followed by the name ending it with ():
    print('Matt is the best')


spam()
spam()
spam()


def cubeNumber(x):
    # in this case we want to pass in a number we want cubed
    # print(x**3)
    # we do not want to leave a print statement but a statement of return. We want to capture the value with return.
    return x**3


a = cubeNumber(3)
print(a)


# get function that takes 3 numbers and returns the sum

def getSum(a, b, c):
    return a + b + c


b = getSum(1, 2, 3)
print(b)


def combineName(first, middle, last):
    return first + " " + middle[0] + " " + last


name = combineName('Matt', 'Jeremy', 'Wong')
print(name)


# Exercise: We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. we are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble

def monkey_trouble(a_smile, b_smile):
    if (a_smile == True) and (b_smile == True):
        return True
    elif (a_smile == False) and (b_smile == False):
        return True
    else:
        return False


print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))

# Exercise: Given two int values, return their sum. Unless the two values are the same, then return double their sum


def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b


print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2))
