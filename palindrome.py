def isPalindrome( s: str) -> bool:
    s = s.lower().replace(" ","")
    new_str = ""
    for char in s:
        if ord(char) >= ord('a') and ord(char) <= ord('z') or ord(char) >= ord('0') and ord(char) <= ord('9'):
            new_str+=char
    if new_str == new_str[::-1]:
        return True    
    return False        



s = "0p"
print(isPalindrome(s))
