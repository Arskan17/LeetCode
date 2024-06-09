class Solution:
    from collections import Counter
    def longestPalindrome(self, s: str) -> int:
        recordLengths = Counter(s)

        evenLetters = sum(even for even in recordLengths.values() if even%2 == 0)
        oddLetters = [odd for odd in recordLengths.values() if odd%2 != 0]

        maxInOdds = max(oddLetters, default=0)
        maxUsableFromOddLetter = (sum(oddLetters) - maxInOdds - (len(oddLetters) - 1)) + maxInOdds

        if not oddLetters:
            return evenLetters
              
        return evenLetters + maxUsableFromOddLetter
