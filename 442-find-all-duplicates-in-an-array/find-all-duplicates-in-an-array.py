class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        jj = []
        ii = {}
        for n in nums:
            if n in ii:
                jj.append(n)
            else:
                ii[n] = 1
        return jj #sorted(jj)