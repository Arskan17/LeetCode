class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # ls = [0] # put 0 in front
        # # given that the last elem in `ls` is always the current sum of the list,
        # # just take that, and sum with the current elem in `nums`.
        # for n in nums[:-1]:
        #     ls.append(ls[-1]+n)


        # # summ the right slice for every index, untill the second to last
        # rs = [sum(nums[i+1:]) for i in range(len(nums)-1)]
        # rs.append(0) # append the 0 to fill

        # return [abs(l-r) for r, l in zip(ls,rs)]

        """New & improved solution"""

        total = sum(nums)
        ans = []
        prev_ls = 0
        for n in nums:
            j = abs(prev_ls - (total - n))
            prev_ls += n
            total -= n

            ans.append(j)
        
        return ans
