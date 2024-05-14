class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        jj = 0
        for i in range(len(digits)):
            jj += (digits[i]*10**(len(digits)-i-1))
        jj += 1
        return [int(i) for i in str(jj)]
            