#Leetcode link: https://leetcode.com/problems/sqrtx/submissions/
# Suresh G --> Python3

class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        res=math.sqrt(x)
        print(res)
        res1="{:.0f}".format(math.floor(res))
        return res1
