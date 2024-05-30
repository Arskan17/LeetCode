class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        jj = set(nums)
        return not len(jj) == len(nums)