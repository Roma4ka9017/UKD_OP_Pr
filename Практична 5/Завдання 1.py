nums = [1, 5, 5, -4, 12, 42, 2]
print(nums)

nums.append(8)
print(nums)

nums.remove(5)
print(nums)

index_12 = nums.index(12)
nums[index_12] = -12
print(nums)

nums.insert(4, -8)
print(nums)

nums.reverse()
print(nums)

nums.clear()
print(nums)