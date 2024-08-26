
def twoSum(numbers, target: int):
    pevmap = {}
    for i,n in enumerate(numbers):
        diff = target - n
        if diff in pevmap:
            return [pevmap[diff]+1,i+1]
        pevmap[n]=i
    return

# nums=sorted([-1,-2,-3,-4,-5])
# print(nums)
# target= -7
nums = [1,2,3,4]
target = 3

def twoSum(numbers, target: int):
    length = len(numbers) -1
    min_length =0
    i= 0
    while i<=length+1:
        print(numbers[min_length]+numbers[length])
        if  numbers[min_length]+numbers[length] == target:
            return [min_length+1,length+1]
        if  numbers[min_length]+numbers[length] < target:
            min_length +=1
            length = length
        if  numbers[min_length]+numbers[length] > target:
            min_length = min_length
            length -= 1
        print("min_length",min_length,"length",length)

        i+=1
print(twoSum(nums,target))
