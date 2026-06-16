nums = [3,5,6,1,2]
nums.sort()
print(nums)

count = 0
for num in nums:
    if num%2 == 0:
        count += 1
print(count)