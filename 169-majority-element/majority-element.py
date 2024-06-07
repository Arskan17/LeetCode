class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        jj = {}
        for i in nums:
            if i not in jj:
                jj[i] = 0
            jj[i] += 1

        for key, value in jj.items():
            if value > len(nums)//2:
                return key
        