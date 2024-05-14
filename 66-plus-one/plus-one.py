class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        jj = 0
        for i in range(n):
            jj += (digits[i]*10**(n-i-1))
        jj += 1
        return [int(i) for i in str(jj)]
            