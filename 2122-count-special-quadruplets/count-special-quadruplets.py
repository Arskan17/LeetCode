class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        # distQ = []
        # for a in range(n):
        #     for b in range(a+1,n):
        #         for c in range(b+1,n):
        #             for d in range(c+1,n):
        #                 if ((nums[a] + nums[b] + nums[c] == nums[d]) & (a < b < c < d)):
        #                     distQ.append([nums[a], nums[b], nums[c], nums[d]])
        # return len(distQ)
        return len([[nums[a], nums[b], nums[c], nums[d]] for a in range(n) for b in range(a+1,n) for c in range(b+1,n) for d in range(c+1,n) if ((nums[a] + nums[b] + nums[c] == nums[d]) & (a < b < c < d))])