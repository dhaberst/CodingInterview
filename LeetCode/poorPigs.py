'''
A program that reverses an integer.

Time complexity: O(N) where N is the number of buckets (this is a generalized upper limit,
  since the growth of (minutesToTest / minutesToDie + 1) ** pigs is exponential therefore
  it will more specifically be related to that.
Space complexity: O(1)
'''
import math

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """     
        pigs = 0
        
        # Essentially we need to find the minutesToTest / minutesToDie+1 which is the
        #  number of tests we can get a pig to do in the time limit. When we start with 0
        #  pigs we see if that number is < buckets. The reason we use the power
        #  is that we think of it as dimensions.
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs +=1
 
        return pigs
    

s = Solution()
print(s.poorPigs(25, 15, 60))
print(s.poorPigs(1000, 15, 60))
print(s.poorPigs(1, 1, 1))