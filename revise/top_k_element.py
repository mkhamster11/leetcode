from collections import defaultdict



def topKFrequent(nums: list[int], k: int) -> list[int]:
    count_dict = dict()
    for num in nums:
        count_dict[num] = 1+count_dict.get(num,0)
    
    freq = [[] for _ in range(len(nums) + 1)]
    for k,v in count_dict.items():
        freq[v].append(k)
    
    res = []
    for i in range(len(nums)-1,-1,-1):
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
