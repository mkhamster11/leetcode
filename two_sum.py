
######### my solutuion 
def twoSum(nums: list[int], target: int) -> list[int]:
    

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!= j:
                print(i,j)
                sum_value = nums[i]+nums[j]
                if sum_value == target:
                    return [i,j]
    return

######### best solution 
def twoSum(nums: list[int], target: int) -> list[int]:
    for i,n in enumerate(nums):
        pevmap = {}
        diff = target - n
        print(diff,n)
        if diff in pevmap:
            return [pevmap[diff],i]
        pevmap[n]=i
        print(pevmap)
    return

nums=[-1,-2,-3,-4,-5]
target=-7


print(twoSum(nums,target))
