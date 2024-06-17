class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        jj = [int(digit) for digit in str(num)]
        num = sum(jj)
        
        return Solution().addDigits(num)