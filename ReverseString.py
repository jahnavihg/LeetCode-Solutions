class Solution:
    def reverseString (self,s):
        def reverse (left,right):
            if left<=right:
                return 
            s[left],s[right]=s[right],s[left]
            reverse(left+1,right-1)
        