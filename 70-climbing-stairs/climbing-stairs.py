import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        staires = {}

        def jello(n:int, staires):
            if (n>2):
                if n not in staires: staires[n] = (jello(n-1, staires) + jello(n-2, staires))
                return staires[n]
            return n
            
        return int(jello(n, staires))
