def remove_duplicate (nums):
    unique=[]
    for num in nums:
        if num not in unique:
            unique.append(num)
    return unique
nums=[2,7,11,15,11,2]
print(remove_duplicate(nums))