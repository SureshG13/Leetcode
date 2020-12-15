#leetcode link: https://leetcode.com/problems/roman-to-integer/
# Suresh G --> Python3
class Solution:
    def romanToInt(self, s: str) -> int:
        s=s[::-1]
        sum=0
        i=0
        while(i<len(s)):
            if s[i]=="I":
                sum+=1
                i+=1
            elif s[i]=="V":
                       if i!=len(s)-1 and s[i+1]=="I":
                            sum+=4
                            i+=2
                       else:
                            sum+=5
                            i+=1
            elif s[i]=="X":
                       if i!=len(s)-1 and s[i+1]=="I":
                            sum+=9
                            i+=2
                       else:
                            sum+=10
                            i+=1
            
            elif s[i]=="L":
                       if i!=len(s)-1 and s[i+1]=="X":
                            sum+=40
                            i+=2
                       else:
                            sum+=50
                            i+=1
            elif s[i]=="C":
                       if i!=len(s)-1 and s[i+1]=="X":
                            sum+=90
                            i+=2
                       else:
                            sum+=100
                            i+=1
            elif s[i]=="D":
                       if i!=len(s)-1 and s[i+1]=="C":
                            sum+=400
                            i+=2
                       else:
                            sum+=500
                            i+=1
            elif s[i]=="M":
                       if i!=len(s)-1 and s[i+1]=="C":
                            sum+=900
                            i+=2
                       else:
                            sum+=1000
                            i+=1
        return sum
            
