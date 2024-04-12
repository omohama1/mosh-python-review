letters = ["a", "b", "c"]

# Add
letters.append("d")
letters.insert(0, "a2")

print(letters)

# Remove
letters.pop()
letters.pop(0)
letters.remove("b")
del letters[0:]
letters.clear()  # removes all items
print(letters)
