#Leetcode link: https://leetcode.com/problems/search-insert-position/
# Suresh G --> Python3

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        
