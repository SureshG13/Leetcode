Leetcode link: https://leetcode.com/problems/maximum-product-subarray/description/
#Suresh G --> Python3


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = float("-inf")
        curr_neg_prod = 1
        running = 1
        for n in nums:
            if n != 0:
                running *= n
                best=max(best,running)
                best=max(best,int(running/curr_neg_prod))
                if curr_neg_prod == 1:
                    if n<0:
                        curr_neg_prod = running
            else:
                running = 1
                curr_neg_prod = 1
                best=max(best,0)
        return best

