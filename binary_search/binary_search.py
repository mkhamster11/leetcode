def search(nums: list[int], target: int) -> int:
    l,r = 0,len(nums)-1
    while l<=r:
        m = l + ((r-l)//2)
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1

nums = [-1,0,2,4,6]
target = 4

print(search(nums,target))
