import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        staires = np.zeros(n+1)
        staires[0] = 1
        staires[1] = 2
        def jello(n:int, staires:list):
            if (staires[n-1] != 0): return staires[n-1]
            else:
                staires[n-1] = jello(n-1, staires) + jello(n-2, staires)
                return staires[n-1]
        return int(jello(n, staires))