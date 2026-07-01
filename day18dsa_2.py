def two_sum(nums, target):
## Two sum problem leetcode
    hashmap = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[nums[i]] = i

nums = [2, 7, 11, 15]
print(two_sum(nums, 9))