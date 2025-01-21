s = "racecar"
t = "carrace"

def isAnagram(s,t):
    unqiue_s = set(s)
    if len(s) != len(t):
        return False
    for char_s in unqiue_s:
        if s.count(char_s) != t.count(char_s):
            return False
    return True



print(isAnagram(s,t))