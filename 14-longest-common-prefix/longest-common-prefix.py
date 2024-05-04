class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        JJ = sorted(strs)
        f = JJ[0]
        l = JJ[-1]
        ret = ""
        for i in range(min(len(JJ[0]), len(JJ[-1]))):
            if f[i] != l[i]:
                return ret
            ret+= f[i]

        return ret
