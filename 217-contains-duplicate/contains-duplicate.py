class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # jj = set(nums)
        # return not len(jj) == len(nums)
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: return True