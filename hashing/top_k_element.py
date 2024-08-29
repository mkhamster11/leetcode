from collections import defaultdict
#### my solution
# def topKFrequent(nums:list, k):
#     hashMap = list()
#     set_nums = set(nums)
#     for num in set_nums:
#         count = nums.count(num)
#         if count >=k:
#             hashMap.append(num)
    
#     return hashMap

###### with hash map 
# def topKFrequent(nums:list, k):
#     hashMap = dict()
#     set_nums = set(nums)
#     res = []

#     for i in range(len(nums),0,-1):
#         hashMap[i] = []

#     for num in set_nums:
#         count = nums.count(num)
#         hashMap[count].append(num)

#     for i in hashMap.values():
#         print(i)
#         if i and len(res) < k:
#             res.extend(i)   

#     return res


def topKFrequent(nums: list[int], k: int) -> list[int]:
    counter = {}

    for n in nums:
        counter[n] = 1 + counter.get(n, 0)
    
    freq = [[] for _ in range(len(nums) + 1)]

    for n, f in counter.items():
        freq[f].append(n)
    
    res = []

    for i in range(len(freq) - 1, -1, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

# nums = [3,1,2,2,3,3,3]
nums=[4,1,-1,2,-1,2,3]

k = 3

# nums = [7,7]
# k = 1
# nums = [1]
# k = 1
print("final",topKFrequent(nums,k))
