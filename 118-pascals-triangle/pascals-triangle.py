class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # s = set()
        jj = [[1]]*numRows
        last = []

        for i in range(numRows):
            j = [1]*(i+1)
            for k in range(1, i):
                j[k] = last[k-1] + last[k]
            last = j
            jj[i] = j
        
        return jj

        # def pasrec(n):
        #     if n == 1: return [1]

        #     tmp = pasrec(n-1)
        #     for i in range(1, n-1):
