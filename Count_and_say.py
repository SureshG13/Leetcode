#leetcode link: https://leetcode.com/problems/count-and-say/
# Suresh G --> Python3
class Solution:
    def countAndSay(self, n):
        return ''.join(self.nextSequence(n, ['1', 'E']))

    def nextSequence(self, n, prevSeq):
        if n == 1:
            return prevSeq[:-1]

        nextSeq = []
        prevDigit = prevSeq[0]
        digitCnt = 1
        for digit in prevSeq[1:]:
            if digit == prevDigit:
                digitCnt += 1
            else:
                nextSeq.extend([str(digitCnt), prevDigit])
                prevDigit = digit
                digitCnt = 1
        nextSeq.append('E')

        return self.nextSequence(n-1, nextSeq)
            
