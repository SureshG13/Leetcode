#link --> https://leetcode.com/problems/majority-element/
# Python3 --> Suresh G

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        j=list(set(nums))
        for i in j:
            if nums.count(i)> n/2:
                return i
        
