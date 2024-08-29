
#### wrong di not understand qs properly .....
# def isValid(s: str) -> bool:
#     parentheses = {"(":")","{":"}","[":"]"}  
    
#     for indx,char in enumerate(s[:int(len(s)/2)]):
#         close_idx = -1
#         close_parentheses = parentheses.get(char,None)
#         if indx !=0:
#             close_idx = -1*indx -1
        
#         if close_parentheses != s[close_idx]:
#             return False

#     return True
s = "[()]"
# s = "([{}])"
# s = "[(])"
s = "{[]()}"

### v2
def isValid(s: str) -> bool:
    stack = []  
    parentheses = {")":"(","}":"{","]":"["}      
    for char in s:
        if char in parentheses:
            if stack and stack[-1] == parentheses[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
        
    
    return True if not stack else False



print(isValid(s))