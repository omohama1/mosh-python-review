numbers = [3, 51, 2, 8, 6]
numbers.sort()
# print(numbers)
numbers.sort(reverse=True)
# print(numbers)
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))

items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]


def sort_item_by_price(item):
    return item[1]


items.sort(key=sort_item_by_price)
print(items)
