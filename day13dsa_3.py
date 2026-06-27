def find_second_largest(arr):
    n = len(arr)
    if n < 2:
        return None
    for i in range(2):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[-2]
numbers = [12, 35, 1, 10, 34, 1]
result = find_second_largest(numbers)
print("The second largest element is:", result) # Output: 34
