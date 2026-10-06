def unique_sorted(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    n = len(unique_nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if unique_nums[j] > unique_nums[j + 1]:
                unique_nums[j], unique_nums[j + 1] = unique_nums[j + 1], unique_nums[j]
    return unique_nums
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))