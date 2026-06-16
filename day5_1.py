#numbers = [32,56,13,3]
#print(max(numbers))
#print(sum(numbers))
#print(min(numbers))

## print otherthan duplicates
nums = [1,2,2,5,3,4,4]
unique = []
for num in nums:
    if num not in unique:
        unique.append(num)
print(unique)
unique.sort()
print(unique)