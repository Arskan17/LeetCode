class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums = [i for i in nums if i != val]
        # # n = len(nums) - len(jj)
        # # for i in range(n):
        # #     jj.append(0)
        # return len(nums)

        i = 0  # Write pointer (tracks non-matching elements)
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]  # Copy non-matching element
                i += 1  # Move write pointer
        return i
                
        