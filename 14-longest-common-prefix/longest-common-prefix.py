class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        JJ = sorted(strs)
        ret = ""
        for i in range(min(len(JJ[0]), len(JJ[-1]))):
            if JJ[0][i] != JJ[-1][i]:
                return ret
            ret+= JJ[0][i]

        return ret
