# BUBBLE SORT
numbers = [5, 3, 8, 4]
n = len(numbers)
for i in range(n):
    for j in range(n - i - 1):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)

## SELECTION SORT
numbers = [64, 25, 12, 22, 11]
n = len(numbers)
for i in range(n):
    minimum = i
    for j in range(i + 1, n):
        if numbers[j] < numbers[minimum]:
            minimum = j
    numbers[i], numbers[minimum] = numbers[minimum], numbers[i]
print(numbers)