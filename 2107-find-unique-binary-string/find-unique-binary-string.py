class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        return next(f'{i:0{n}b}' for i in range(2**n) if f'{i:0{n}b}' not in nums)