# Leetcode link: https://leetcode.com/problems/valid-palindrome/
# Suresh G --> Python3

class Solution:
    def isPalindrome(self, s: str) -> bool:
    	s = [i for i in s.lower() if i.isalnum()]
    	return s == s[::-1]
