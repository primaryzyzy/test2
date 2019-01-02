class Solution(object):
    def reverse(self, x):
        if x < 0:
            a = str(x)[:0:-1]
            b =int( "-" + a)
        else:
            b = int(str(x)[::-1])
        if b > -2**31 and b < 2**31-1:
            return b
        else:
            return 0
        
if __name__ == "__main__":


    s = Solution()

    print( s.reverse(123))

    print( s.reverse(-123))
    print( s.reverse(120))

