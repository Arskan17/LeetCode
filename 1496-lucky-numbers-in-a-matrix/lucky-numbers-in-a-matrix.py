class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minsInRows = [min(row) for row in matrix]
        maxsInColumns = []
        for columnIndex in range(len(matrix[0])):
            columnElems = [row[columnIndex] for row in matrix]
            maxsInColumns.append(max(columnElems))

        return [elem for elem in minsInRows if elem in maxsInColumns]