class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        while n:
            if n>i:
                i+=1
                n = n-i
            else: break
        return i
