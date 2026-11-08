# Find the largest number in a list

nums = [10, 25, 7, 40, 15]

largest = nums[0]

for num in nums:
    if num > largest:
        largest = num

print(largest)
