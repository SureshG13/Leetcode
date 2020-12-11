#Leetcode link: https://leetcode.com/problems/palindrome-number/
# Suresh G --> Python 3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
