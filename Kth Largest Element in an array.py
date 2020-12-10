#Leetcode link : https://leetcode.com/problems/kth-largest-element-in-an-array/
#Suresh G --> Python 3

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums.reverse()
        return nums[k-1]
