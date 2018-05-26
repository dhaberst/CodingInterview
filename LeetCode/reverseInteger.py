'''
A program that reverses an integer.

Time complexity: O(N) where N is the number of digits in x.
Space complexity: O(N) where N is the number of digist in x.
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNeg = False
        
        if x >= 0:       
            splitx = [i for i in str(x)]

        else:
            isNeg = True
            splitx = [i for i in str(x)][1:]

            
        splitx.reverse()
        
        result = int(''.join(splitx))
        
        if result <= 2**31 - 1:
        
            if isNeg:
                return -result

            return result
    
        return 0

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(2**32))