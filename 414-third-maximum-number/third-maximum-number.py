class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinctNumbers = set(nums)

        if len(distinctNumbers) < 3:
            return max(distinctNumbers, default = 0)
        
        return sorted(distinctNumbers)[-3]
