class Solution:
    def climbStairs(self, n: int) -> int:
        staires = {}
        
        '''With recursion'''

        # def jello(n:int, staires):
        #     if (n>2):
        #         if n not in staires: staires[n] = (jello(n-1, staires) + jello(n-2, staires))
        #         return staires[n]
        #     return n
        # return int(jello(n, staires))

        '''with loop'''

        staires[0] = 1
        staires[1] = 2
        for i in range(2, n):
            staires[i] = staires[i-1] + staires[i-2]
        return staires[n-1]
