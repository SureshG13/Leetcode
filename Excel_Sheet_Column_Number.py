#  Link: https://leetcode.com/problems/excel-sheet-column-number/
# Suresh G --> Python3

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for c in columnTitle:
            res = res*26 + ord(c)-ord('A')+1
        return res
            
