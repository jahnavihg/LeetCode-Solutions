def RotateByK(nums,k):
    n=len(nums)
    temp=[]*n
    for i in range(n):
        temp[(i+k)%n]==nums[i]
    for i in range(n):
        nums[i]=temp[i]