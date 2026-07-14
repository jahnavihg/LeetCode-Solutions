class Solution:
    def fabonacci(self,n):
        if n <=1:
            return n
        return self.fabonacci(n-1)+self.fabonacci(n-2)