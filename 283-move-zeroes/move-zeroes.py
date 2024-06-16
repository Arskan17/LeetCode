class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        withoutZeros = [num for num in nums if num != 0]

        for index, num in enumerate(withoutZeros):
            nums[index] = num
        for index in range(len(withoutZeros), len(nums)):
            nums[index] = 0