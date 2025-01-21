nums = [1, 2, 3, 3]


def dup_integer(nums):
    rep_map =[]
    for i in nums:
        if i in rep_map:
            return True
        else:
            rep_map.append(i)
    return False

print(dup_integer(nums))