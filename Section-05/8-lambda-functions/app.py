numbers = [3, 51, 2, 8, 6]
numbers.sort()
# print(numbers)
numbers.sort(reverse=True)
# print(numbers)
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))

items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]


items.sort(key=lambda item: item[1])
print(items)
