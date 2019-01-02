class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            return x == int(str(x)[::-1])
        
        

s = Solution()
print(s.isPalindrome(-121))

