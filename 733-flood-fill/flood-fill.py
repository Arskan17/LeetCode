class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # length = len(image)
        # width = len(image[0])

        # if length == 1 and width ==1:
        #     return [[color]]

        # c = image[sr][sc]


        # record = {}
        # for l in range(length):
        #     for w in range(width):
        #         if w < width-1 and image[l][w] == c and (image[l][w+1] == c or image[l][w-1] == 1):
        #             record[(l,w)] = color

        #         elif l < length-1 and image[l][w] == c and (image[l+1][w] == c  or image[l-1][w] == 1):
        #             record[(l,w)] = color

        #         elif w == width-1 and image[l][w] == c and image[l][w-1] == c:
        #             record[(l,w)] = color

        #         elif l == length-1 and image[l][w] == c and image[l-1][w] == c:
        #                 record[(l,w)] = color


        # for l in range(length):
        #     for w in range(width):
        #         if (l,w) in record:
        #             image[l][w] = color

        # image[sr][sc] = color

        # return image


        original_color = image[sr][sc]
        if original_color == color:
            return image
            
        def dfs(r, c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != original_color:
                return
            
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        dfs(sr, sc)
        return image
