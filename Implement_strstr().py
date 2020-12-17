#Leetcode link: https://leetcode.com/problems/implement-strstr/
# Suresh G --> Python3

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack=="" and needle=="":
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1
        
