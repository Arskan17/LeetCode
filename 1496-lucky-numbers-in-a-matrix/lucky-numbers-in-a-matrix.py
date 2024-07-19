class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minsOfRows = [min(row) for row in matrix]
        maxOfColumns = []
        for columnIndex in range(len(matrix[0])):
            columnElems = [row[columnIndex] for row in matrix]
            maxOfColumns.append(max(columnElems))

        return [elem for elem in minsOfRows if elem in maxOfColumns]