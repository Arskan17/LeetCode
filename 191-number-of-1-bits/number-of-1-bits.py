class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        jj = format(n, 'b')
        for j in jj:
            if int(j) == 1: i+=1
        return i
        