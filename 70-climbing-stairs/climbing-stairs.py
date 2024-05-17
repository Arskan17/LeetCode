import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        staires = np.zeros(n+1)
        staires[0] = 1
        staires[1] = 2
        def jello(n:int, staires):
            if (n>2):
                if (staires[n-1] != 0): return staires[n-1]
                staires[n-2] = jello(n-1, staires)
                staires[n-3] = jello(n-2, staires)
                staires[n-1] = (staires[n-2] + staires[n-3])
                return staires[n-1]
            return staires[n-1]
        return int(jello(n, staires))
