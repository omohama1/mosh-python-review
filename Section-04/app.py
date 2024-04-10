# Sections 1 & 2
"""
def greet(first_name, last_name):
    print(f"Hi there, {first_name} {last_name}")
    print("Welcome aboard")
"""

# Section 3
# 1- Perform a task
# 2- Return a value
# greet("Commissar", "Cannoli")  # Peforms a task
round(1.9)  # Returns a value


def get_greeting(name):
    return f"Hi {name}"


# message = get_greeting("Mosh")
# file = open("content.txt", "w")
# file.write(message)

# print(greet("Omar", "M"))  # returns None

# Section 4
def increment(number, by=1):
    return number + by


result = increment(2, 1)

# print(result) # prints 3

# print(increment(2, by=1)) # prints 3

# Section 5
# print(increment(2))  # prints 3
# print(increment(2, 5))  # prints 7

# Section 6


def multiply(*numbers):
    product = 1
    for number in numbers:
        product *= number
    return product


# print(multiply(2, 3, 4, 5))

numbers_list = [2, 3, 4, 5]  # list
numbers_tuple = (2, 3, 4, 5)  # tuple

# Both tuples and lists are iterable

# Section 7


def save_user(**user):
    print(user["name"])


# save_user(id=1, name="John", age=22)

user = {'id': 1, 'name': 'John', 'age': 22}  # dictionary

# Section 8


def greet(name):
    message = f"Hi {name}"
    return message


message = greet("cannoli")
# print(message)

# Section 9
# print("Start")
# print(multiply(1, 2, 3))  # result == 6

# Section 10 # windows shortcuts

# Section 11 # mac shortcuts

# Section 12 - Exercise
# divisible by 3 - fizz
# divisible by 5 - buzz
# divisible by 3 and 5 - fizzbuzz


def fizz_buzz(input):
    # if divisible by 3 and 5
    if (input % 3 == 0 and input % 5 == 0):
        return "FizzBuzz"
    # if divisible by 3
    if input % 3 == 0 and input % 5 != 0:
        return "Fizz"
    # if divisible by 5
    if input % 5 == 0 and input % 3 != 0:
        return "Buzz"
    return input


print(fizz_buzz(15))
print(fizz_buzz(20))
print(fizz_buzz(30))
print(fizz_buzz(10))
print(fizz_buzz(6))
print(fizz_buzz(5))
print(fizz_buzz(3))
print(fizz_buzz(1))
print(fizz_buzz(7))
