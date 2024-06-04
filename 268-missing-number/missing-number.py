class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # if (len(nums)==1 and nums[0]==1): return 0
        jj = []
        for i in range(1, len(nums)+1):
            if (i not in nums): return i
            else: jj.append(i)
        return 0
        