class Solution:
    def hammingWeight(self, n: int) -> int:
        i = 0
        jj = format(n, 'b') # format() converts its first param depending on its second, in this case 'b' for binary

        for j in jj:
            if int(j) == 1:
                i += 1

        return i
        