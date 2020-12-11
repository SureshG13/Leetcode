#Leetcode link: https://leetcode.com/problems/median-of-two-sorted-arrays/
#Suresh G --> Python3

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=nums1+nums2
        l=sorted(l)
        a=len(l)
        b=a//2
        if a%2==0:
            return (l[b-1]+l[b])/2
        else:
            return (l[b])
