#Leetcode link: https://leetcode.com/problems/valid-parentheses/
# Suresh G--> Python3
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==0:
            lis=[]
            for i in range(len(s)):
                if s[i]=="{" or s[i]=="(" or s[i]=="[":
                    lis.append(s[i])
                elif s[i]==")"and len(lis)>=1 and lis[-1]=="(":
                    lis.pop()
                elif s[i]=="}"and len(lis)>=1 and lis[-1]=="{":
                    lis.pop()
                elif s[i]=="]" and len(lis)>=1 and lis[-1]=="[":
                    lis.pop()
                else:
                    lis.append(s[i])
            l=len(lis)
            if l>0:
                return False
            else:
                return True
        else:
            return False
        
