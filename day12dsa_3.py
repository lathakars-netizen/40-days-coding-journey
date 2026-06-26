def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [10, 20, 30, 40]
print(linear_search(numbers, 30))