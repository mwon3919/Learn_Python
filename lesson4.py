#list and tuples
# list store a collection of ints, strings, etc. tuple is a slightly different version of that.

grocery_list = ['milk', 'avocados', 'hot pockets']

# adding items to list
grocery_list.append('oreos')
grocery_list.append('chicken')
grocery_list.append('eggs')


# removing items
grocery_list.pop()  # remove last item of list

# remove a specific item, you will use indexing. A position of the list. For example if you want to remove avocados, you first look at the index of the list. In this case avocado is in the second position which is index 1. (0 based indexing)

grocery_list.pop(1)

'''indexing
['milk','avocados','hot pockets','oreos','chicken','eggs']
    0       1           2           3       4       5
    -6      -5          -4          -3      -2      -1
'''

position = [100, 300]
print(position[1])

# in addition to indexing one element we can splice index to get a range of indexes.
print(grocery_list[1:5])  # grocery_list(included,not included)

# get length of list
print(len(grocery_list))

# inserting item in a specific location
grocery_list.insert(2, 'silverware')

# find index of specific item
print(grocery_list.index('oreos'))

print(grocery_list)

# numeric list
grades = [100, 34, 72, 95, 93, 84, 87, 87, 100, 100]


print(grades)
# useful commands for a list of numbers

# sort items in increasing order
grades.sort()
print(grades)

# reverse order
grades.reverse()
print(grades)


# count specific number
print(grades.count(100))


# differnce between list and tuples
# instead of [ ] we use ( )

#Mutable - Append, pop, remove, etc
values = [1, 2, 3]  # list of three values

# Immutable - set object. Values stored and structur does not change
values = (1, 2, 3)  # tuple of three values


def update(x, y, z):
    x = x + 5
    y = y - 3
    z = z + 10

    return (x, y, z)


print(update(10, 10, 10))

x, y, z = update(10, 10, 10)

print(x)

grades = [95, 93, 80, 82]
# maybe, one of the students came up and said grades are improper and want to reevauate a grade
print(grades)
grades[2] = 90
print(grades)


names = ['ben', 'jerry', 'bob', 'joe', 'xavier', 'tyranataur', 'shaquavius', 'matt', 'pegasus']

# I want my function to see if my name is included


def check_for_name(name, names):
    if name in names:
        return True
    else:
        return False


print(check_for_name('matt', names))
