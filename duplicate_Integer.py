



# # Solution-1
# def hasDuplicate(nums: list[int]) -> bool:
#     temp_list = sorted(nums)
#     for indx,num in enumerate(temp_list):
#         try:
#             if num == temp_list[indx+1]:
#                 return True
#         except IndexError:
#             return False

#     return False


# ## Solution-2 
# def hasDuplicate(nums: list[int]) -> bool:
#     temp_list = sorted(nums)
#     for indx,num in enumerate(temp_list[:-1]):
#         if num == temp_list[indx+1]:
#             return True
#     return False


###Solution-3 Best one with hashset 
def hasDuplicate(nums: list[int]) -> bool:
    tempset = set()
    for num in nums:
        if num in tempset:
            return True
        tempset.add(num)
    return False

# def hasDuplicate(nums: list[int]) -> bool:
#     tempset = set(nums)
#     if len(tempset) == len(nums):
#         return False
#     return True

print(hasDuplicate([1,2,3,4,5,5]))