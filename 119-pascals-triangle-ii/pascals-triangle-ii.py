class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        last = jj = []

        for i in range(rowIndex+1):
            jj = [1]*(i+1)

            for j in range(1, i):
                jj[j] = last[j-1] + last[j]
            
            last = jj
        
        return jj