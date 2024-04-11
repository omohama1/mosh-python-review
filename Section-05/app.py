letters = ["a", "b", "c"]
matrix = [[0,1], [2,3]]
zeroes = [0]* 5
combined = zeroes + letters
numbers = list(range(20))
chars = list ("Hello World")
#print(numbers)
#print(chars)

letters = ["a", "b", "c", "d"]
letters[0] = "A"
# print(letters[0:]) # prints ['A', 'b', 'c', 'd']
# print(letters[0:3]) # prints ['A', 'b', 'c']
# print(letters[::2]) # prints ['A', 'c']

numbers = list(range(20))
# print(numbers[::2]) # prints only even numbers
# print(numbers[::-1]) # prints list in reverse

numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third  = numbers[2]

#Easier way to do this
first, second, third= numbers # list unpacking
numbers = [1,2,3,4,5,6]
# first, second = numbers # throws error
first, *other, last = numbers 
# print(first) # first number
# print(other) # everything after second item
# print (last)

letters = ["a", "b", "c"]

for letter in enumerate(letters):
    print(letter)