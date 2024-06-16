class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)-1):
            if nums[index] == nums[index+1]:
                num = nums[index] * 2
                nums[index] = num
                nums[index+1] = 0

        withoutZeros = [num for num in nums if num != 0]

        for index,num in enumerate(withoutZeros):
            nums[index] = num

        for index in range(len(withoutZeros), len(nums)):
            nums[index] = 0

        return nums