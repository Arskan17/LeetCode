class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3: return max(nums)

        nums = sorted(nums)

        j = 1
        k = 0
        for i in range(len(nums)-2, -1, -1):
            if j == 3: return k

            if nums[i] != nums[i+1]:
                j += 1
                k = nums[i]
        return k
