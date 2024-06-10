# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n < 2: return n

        # import numpy
        upper = n
        lower = 0

        while lower <= upper:
            isIt = guess((lower + upper) // 2)
            if isIt == 0:
                return (lower + upper) // 2
            elif isIt == -1:
                upper = ((lower + upper) // 2) - 1
            elif isIt == 1:
                lower = ((lower + upper) // 2) + 1

        return n