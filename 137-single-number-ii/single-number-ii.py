class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        jj = {}
        for n in nums:
            if n in jj:
                jj[n] += 1
                if jj[n] == 3:
                    del jj[n]
            else:
                jj[n] = 1
        for k, v in jj.items():
            if v == 1: return k