import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        staires = np.zeros(n+1)
        def jello(n:int, staires):
            if (n>2):
                if (staires[n] != 0): return staires[n]
                staires[n-1] = jello(n-1, staires)
                staires[n-2] = jello(n-2, staires)
                staires[n] = (staires[n-2] + staires[n-1])
                return staires[n]
            return n
        return int(jello(n, staires))
