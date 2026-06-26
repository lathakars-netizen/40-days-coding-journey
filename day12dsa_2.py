numbers = [8, 15, 3, 22, 9]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)


numbers = [8, 15, 3, 22, 9]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest:", smallest)