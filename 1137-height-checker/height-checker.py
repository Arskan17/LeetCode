class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        wrongHeight = 0
        for i, height in enumerate(heights):
            if height != expected[i]:
                wrongHeight += 1
        
        return wrongHeight
        