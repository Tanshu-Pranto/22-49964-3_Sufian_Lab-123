items = [10, 20, 30, 20, 50]
unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)

print(unique_items)