import numpy as np
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets = []
        seen = set()

        # checks if all elements are zero first
        if (all(x == 0 for x in nums[1:])):
            return [[0,0,0]]

        # then checks if all elements are identical second
        if (all(x == nums[0] for x in nums[1:]) and nums[0]!=0):
            return []

        for i in range(n):
            # Pre-calculate the negative of the current element for faster sum checks
            target = -nums[i]

            # Use a set for efficient membership checks during filtering
            for j in range(i + 1, n):
                complement = target - nums[j]
                if complement in seen:
                    triplets.append([nums[i], nums[j], complement])
            seen.add(nums[i])
        JK = [sorted(i) for i in triplets]
        return [list(i) for i in set(tuple(i) for i in JK)]
        


