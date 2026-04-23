class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        record = {}
        invalid_record = [0]*len(mat[0])
        for i in mat:
            if sum(i) == 1:
                for jndex, j in enumerate(i):
                    if j == 1:
                        if jndex not in record:
                            record[jndex] = 0
                        record[jndex] += 1
            else:
                for jndex, j in enumerate(i):
                    if j==1:
                        invalid_record[jndex] = 1

        return sum([1 for k, v in record.items() if invalid_record[k]==0 and v == 1])
