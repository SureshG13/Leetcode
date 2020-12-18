#Leetcode link: https://leetcode.com/problems/length-of-last-word/
# Suresh G --> Python3

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr=[]
        arr=list(map(str,s.split()))
        if len(arr)>=1:
            return len(arr[-1])
        else:
            return 0
            
