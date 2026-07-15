class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res = []
        for n in nums:
            idx = abs(n) - 1
            
            # If the value at this index is already negative, we've seen 'n' before!
            if nums[idx] < 0:
                res.append(abs(n))
            else:
                # Otherwise, mark it as seen by making it negative
                nums[idx] = -nums[idx]
                
        return res