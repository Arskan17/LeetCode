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

        # loop through the dictionary untill we find a key who's value is 1, return that key.        
        # for k, v in jj.items():
        #     if v == 1: return k
        return next(iter(jj))