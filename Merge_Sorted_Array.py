#Leetcode link: https://leetcode.com/problems/merge-sorted-array/submissions/
# Suresh G --> Python3

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[:n]
        nums1.sort()
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
