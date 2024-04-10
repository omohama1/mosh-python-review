import math

COURSE_NAME = "The \"Muscular\" Course"
"""
students_count = 1000
rating = 4.99
is_published = False
course_name = "The \"Muscular\" Course"
print(students_count)

course_name_length = len(course_name)
print(course_name)
print(course_name_length)

print(course_name[4:14])
first = "Andie"
last = "De Castro Lima"
full = f"{first} {last}"
expression = f"{len(first)} {5/2}"
print(full)
print(expression)
"""
# Escape characters
# \" \' \n \\


# Section 2-6
"""
print(course_name.upper())
print(course_name.lower())
print(course_name.title())
print(course_name.find("z"))
print(course_name.find("ourse"))
print(course_name.replace("Course", "Class"))
print("Musc" in course_name)
print("lame" in course_name)
print(course_name)
"""
# Section 2-7
"""
x = 1
x = 1.1
x = 1 + 2j  # a + bi
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
x = 10
x += 3  # this is the same as x = x + 3
"""
# Section 2-8
"""
print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))
print(math.floor(2.2))
"""
# Section 2-9
"""
x_string = input("x: ")
print(type(x_string))
x = int(x_string)
print(type(x))
y = x + 1
print(f"x: {x}, y: {y}")
"""
# Falsy Values: "" , 0 , None
# Truthy Values: Everything else


# Section 2-10 - Quiz


# Section 3-1
ord("b")  # returns 98
ord("B")  # returns 66
"BAG" < "bag"  # returns true

# Section 3-2
"""
temperature = 25
if temperature > 30:
    print("it's fuckin hot")
elif temperature > 20:
    print("it's OK")
else:
    print("it's fuckin cold")
print("done")
"""
# Section 3-3 - Ternary operator
"""
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

# Ternary operation
message = "Eligible" if age >= 18 else "Not eligible"
print(message)
"""
# Section 3-4
"""
high_income = False
good_credit = True
student = True
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
"""

# Section 3-5
"""
high_income = False
good_credit = True
student = True
if (high_income or good_credit) and not student:  # Logical operators are short circuit
    print("Eligible")
else:
    print("Not eligible")
"""

# Section 3-6
# age should be between 18 and 65
"""
age = 22
if age >= 18 and age < 65:
    print("Eligible")

if age <= age < 65:
    print("Really Eligible")
"""

# Section 3-7 Quiz

# Section 3-8 For loops
"""
for number in range(10):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(0, 3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 10, 2):
    print("Attempt", number + 1, (number + 1) * ".")
"""

# Section 3-9
"""
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times. Failed")
"""

# Section 3-10 - Nested loops
"""
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
"""

# Section 3-11 - Iterables
"""
print(type(5))
print(type(range(5)))
"""

# Iterable
# for x in range(5):
# for x in "Python":

# Section 3-12 - While Loops
"""
number = 100
while number > 0:
    print(number)
    number -= 10

command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)
"""

# Section 3-13 - Infinite Loops
"""
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
"""

# Section 3-14 - Exercise
"""
x = 2
count = 0
while x <= 10:
    print(x)
    if (x % 2 == 0):
        count += 1
    x += 2
print(f"We have {count} even numbers")

count = 0
for number in range(1, 10):
    if (number % 2) == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
"""
