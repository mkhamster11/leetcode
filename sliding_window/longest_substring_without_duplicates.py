

#### my solution  
# def lengthOfLongestSubstring( s: str) -> int:
#     max_length= len(s)
#     if max_length > 0: 
#         sub_list ={}
#         for i in range(0,max_length):
#             for j in range(1,max_length+1):
#                 sublist = s[i:j]
#                 no_du =set(sublist)
#                 if len(sublist) == len(no_du) and i != j:
#                     sub_list[f"{no_du}"]= len(no_du)
#         maxSub = max(sub_list.values())
#         return maxSub
#     else:
#         return 0
    
#### best not working in leet code 
def lengthOfLongestSubstring(s: str) -> int:
    chr_set = set()
    l=0
    res =0
    for r in range(len(s)):
        while s[r] in chr_set:
            chr_set.remove(s[1])
            l+=1
        chr_set.add(s[r])
        res = max(res, r-l+1)
    return res


### leet code 
def lengthOfLongestSubstring(s: str) -> int:
    dict = {}
    b_pointer = 0
    a_pointer = 0
    maxx = 0
    while a_pointer < len(s) and b_pointer < len(s):
        if s[b_pointer] not in dict:
            dict[s[b_pointer]] = 1
            b_pointer +=1
            maxx = max(maxx,b_pointer-a_pointer)
        else:  
            del dict[s[a_pointer]]
            a_pointer +=1


    return maxx
s = "zxyzxyz"
s="pwwkew"
# s="abcabcbb"
s =" "
# s= "au"
print(lengthOfLongestSubstring(s))