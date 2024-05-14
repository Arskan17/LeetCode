class Solution:
    def ajj(i, j, c):
        if (i==1 and j==1 and c==1):
            return (1,1)
        elif ((i==1 and j==1 and c==0) or (i==1 and j==0 and c==1) or (i==0 and j==1 and c==1)):
            return (0,1)
        elif ((i==1 and j==0 and c==0) or (i==0 and j==1 and c==0) or (i==0 and j==0 and c==1)):
            return (1,0)
        elif (i==0 and j==0 and c==0):
            return (0,0)

    def addBinary(self, a: str, b: str) -> str:
        def ajj(i, j, c):
            if (i==1 and j==1 and c==1):
                return (1,1)
            elif ((i==1 and j==1 and c==0) or (i==1 and j==0 and c==1) or (i==0 and j==1 and c==1)):
                return (0,1)
            elif ((i==1 and j==0 and c==0) or (i==0 and j==1 and c==0) or (i==0 and j==0 and c==1)):
                return (1,0)
            elif (i==0 and j==0 and c==0):
                return (0,0)

        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        # if (len(a) == n):
        #     for i in range(n-len(b)):
        #         b = reversed(b)
        #         b += '0'
        #         b = reversed(b)
        # else:
        #     for i in range(n-len(a)):
        #         a = reversed(a)
        #         a += '0'
        #         a = reversed(a)

        c = 0
        r = ""
        for i in range(n-1, -1, -1):
            jj = ajj(int(a[i]), int(b[i]), c)
            r += str(jj[0])
            c = jj[1]
        if (c==1):
            r += '1'
        rj = ""
        for i in r[::-1]:
            rj += i
        return rj

        