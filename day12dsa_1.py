##Linear Search
##Linear Search checks each element one by one.
numbers = [10, 20, 30, 40, 50]
target = 30
for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index", i)
        break


##Binary Search
##Binary Search works only on sorted arrays.
numbers = [10, 20, 30, 40, 50]
target = 40

low = 0
high = len(numbers) - 1
while low <= high:

    mid = (low + high) // 2
    if numbers[mid] == target:
        print("Found at index", mid)
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1