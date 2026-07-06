class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        length = len(grid)
        L = 0
        E = 0
        for l in range(length):
            for e in range(width):
                if grid[l][e] == 1:
                    L +=1
                    if (e+1 < width):
                        if grid[l][e+1] == 1:
                            E += 1
                    if (l+1 < length):
                        if grid[l+1][e] == 1:
                            E += 1



        return (4*L)-(2*E)
                    
