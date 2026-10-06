def min_max(nums):
    if len(nums) == 0:
        raise ValueError("Список пуст")
    minimum = nums[0]
    maximum = nums[0] 
    for num in nums:
        if num < minimum:
            minimum = num
        if num > maximum:
             maximum = num
    return (minimum, maximum)
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([]))