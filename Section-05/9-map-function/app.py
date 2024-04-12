items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)]


# prices = []
# for item in items:
#     prices.append(item[1])

# print(prices)

prices = map(lambda item: item[1], items)
for item in prices:
    print(item)
# Alternatively
pricesList = list(map(lambda item: item[1], items))
print(pricesList)
