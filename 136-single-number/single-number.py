class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) == 1: return nums[0] # Base case if size of list is 1

        if nums[0] != nums[1]: return nums[0] # second case if the first elem is the single one
        if nums[-1] != nums[-2]: return nums[-1] # third case if the last elem is the single one

        for i in range(1, len(nums)-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]
