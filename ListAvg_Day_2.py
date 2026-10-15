def average(nums):
    print("DEBUG nums =", nums)
    if not nums:
        return 0
    return sum(nums) / len(nums)
print(average([]))
print(average([2, 4]))

print(average([2, 4, 5]))
print(average(['sdt','sdt', 'sdt']))