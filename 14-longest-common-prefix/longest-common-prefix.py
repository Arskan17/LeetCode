class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        n = min(len(strs[0]), len(strs[-1]))
        f = strs[0]
        l = strs[-1]
        ret = ""
        for i in range(n):
            if f[i] != l[i]:
                return ret
            ret+= f[i]

        return ret
