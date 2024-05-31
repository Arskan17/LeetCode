class Solution:
    def isHappy(self, n: int) -> bool:
        if n != 1 and n!=7 and n<10: return False

        jj = set()

        def sqr(n):
            i = 0

            while n:
                i += (n%10)**2
                n = n//10

            return i

        while n not in jj:
            if n == 1: return True

            jj.add(n)
            n = sqr(n)


        # jj = set()
        # def isit(n, jj):
        #     if n == 1: return True

        #     j = 0
        #     while n:
        #         j += (n%10)**2
        #         n = n//10

        #     if j in jj: return False
        #     jj.add(j)
        #     isit(j, jj)

        # isit(n, jj)