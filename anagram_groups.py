from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list) # mapping charCount to List of Anagrams

    for s in strs: 

        count = [0] * 26 #a ... z
        for c in s: 
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s) 
        print(count,res[tuple(count)],ord("a"))

    return list(res.values()) 






#Input: 
strs = ["act","pots","tops","cat","stop","hat"]

# Output: 
output =[["hat"],["act", "cat"],["stop", "pots", "tops"]]


print(groupAnagrams(strs))