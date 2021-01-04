# Leetcode link: https://leetcode.com/problems/ransom-note/
# Suresh G --> Python3

class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
    	return not any(r.count(i) > m.count(i) for i in set(r))
