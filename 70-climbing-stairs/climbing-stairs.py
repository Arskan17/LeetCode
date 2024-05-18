class Solution:
    def climbStairs(self, n: int) -> int:
        '''With recursion'''

        # staires = {}
        # def jello(n:int, staires):
        #     if (n>2):
        #         if n not in staires: staires[n] = (jello(n-1, staires) + jello(n-2, staires))
        #         return staires[n]
        #     return n
        # return int(jello(n, staires))

        '''with loop'''

        stairesl = [0]*(n+1)
        stairesl[0] = 1
        stairesl[1] = 2
        for i in range(2, n):
            stairesl[i] = stairesl[i-1] + stairesl[i-2]
        return stairesl[n-1]
