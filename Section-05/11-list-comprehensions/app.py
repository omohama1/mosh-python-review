items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)]

pricesList = list(map(lambda item: item[1], items))
print(pricesList)

# Map using list comprehension
prices = [item[1] for item in items]
print(prices)

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

# Filter using list comprehensions
filteredComprehension = [item for item in items if item[1] >= 10]
print(filteredComprehension)
