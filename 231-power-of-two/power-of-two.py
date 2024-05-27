class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0: return False
        for i in range(32):
            if 2**i == n: return True
        # import math
        # if math.log(n, 2) == 2**math.log(n, 2): return True

        return False
        