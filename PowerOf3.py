class Solution
def Power3(self,n:int):
    if n==1:
        return True
    if n<=0 or n%3==0:
        return self.Power3(n//3)
