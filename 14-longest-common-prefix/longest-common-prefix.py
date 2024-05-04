class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        JJ = sorted(strs)
        n = len(JJ[0]) # min(len(JJ[0]), len(JJ[-1]))
        f = JJ[0]
        l = JJ[-1]
        ret = ""
        for i in range(n):
            if f[i] != l[i]:
                return ret
            ret+= f[i]

        return ret
