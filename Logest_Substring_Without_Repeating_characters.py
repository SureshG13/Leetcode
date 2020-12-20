#Leetcode link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Suresh G --> Python3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        else:
            count=0
            for i in range(len(s)-1):
                st=s[i]
                for j in range(i+1,len(s)):
                    if s[j] not in st:
                        st+=s[j]
                    else:
                        break
                c=len(st)
                if c>count:
                    count=c
            return count
        
