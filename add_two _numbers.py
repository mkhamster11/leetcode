def addTwoNumbers(l1, l2):
    
    str1 = str(int("".join(map(str, l1)))+int("".join(map(str,l2))))[::-1]
    return list(map(int,str1))
l1 =[2,4,3]
l2 = [5,6,4]
print(addTwoNumbers(l1, l2))
