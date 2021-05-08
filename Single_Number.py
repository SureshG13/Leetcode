#link-->  https://leetcode.com/problems/single-number/
#Python-3 --> Suresh G

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        j=list(set(nums))
        for i in j:
            if nums.count(i)==1:
                return i
