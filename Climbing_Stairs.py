#Leetcode link: https://leetcode.com/problems/climbing-stairs/submissions/
# Suresh G --> Python3

class Solution:
    def climbStairs(self, n: int) -> int:
        a=[]
        a.append(1)
        a.append(2)
        print(a)
        for i in range(2,n):
            ans=a[i-1]+a[i-2]
            a.append(ans)
        return a[n-1]
