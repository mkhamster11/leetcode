def twoSum(nums, target):
    max_nums=len(nums)
    for i in range(max_nums):
        for j in range(max_nums):
            if i!=j:
                sum_temp = nums[i]+nums[j]
                if sum_temp ==target:
                    return [i,j]
    return[]


nums = [3,5,5,6]
target = 10

print(twoSum(nums,target))
