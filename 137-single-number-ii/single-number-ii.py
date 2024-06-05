class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        jj = {}
        # Iterate through the list and add keep count of the number of times each element appears, by using a dictionary
        for n in nums:
            if n in jj:
                jj[n] += 1
                # if jj[n] == 3:
                #     del jj[n]
            else: jj[n] = 1

        # loop through the dictionary untill we find a key who's value is 1, return that key.        
        for k, v in jj.items():
            if v == 1: return k
        # return next(iter(jj), None)