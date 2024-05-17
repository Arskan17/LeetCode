import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        staires = np.zeros(n+2)
        staires[1] = 1
        staires[2] = 2
        def jello(n:int, staires:list):
            if (staires[n] != 0): return staires[n]
            else:
                staires[n] = jello(n-1, staires) + jello(n-2, staires)
                return staires[n]
        return int(jello(n, staires))