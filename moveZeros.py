def movezeroes(nums):
    temp=[]
    for num in nums:
        if num!=0:
            temp.append(num)
    if len(temp) < len(nums):
        temp.append(0)
    return temp
nums=[0,4,5,6,0,2]
print(movezeroes(nums))