# repeating counter
def count_frequency(i):
    hash_map = {}
    for num in i:
        hash_map[num] = hash_map.get(num, 0) + 1
    return hash_map
arr = [1, 2, 2, 3, 1, 4]
print(count_frequency(arr))
