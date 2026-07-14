class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # record = set(nums)
        # return [i for i in range(1, len(nums)+1)  if i not in record]
        
        """Solution with better space complexity"""
        for n in nums:
            index = abs(n) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        return [i + 1 for i, val in enumerate(nums) if val > 0]