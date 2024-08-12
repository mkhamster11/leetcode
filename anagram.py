
### my Solution 
def isAnagram(s: str, t: str) -> bool:
    distint_words = set()
    if len(s) != len(t):
        return False

    for word in s:
        if word not in distint_words:
            distint_words.add(word)
            if s.count(word) != t.count(word):
                return False
    return True

###Solution-2 

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    if sorted(s) != sorted(t):
        return False
    
    return True

s = "aa"
t = "ab"
print(isAnagram(s,t))