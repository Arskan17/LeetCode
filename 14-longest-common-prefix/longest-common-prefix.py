class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        strs = sorted(strs)
        f = strs[0]
        l = strs[-1]
        n = min(len(f), len(l))
        for i in range(n):
            if f[i] != l[i]:
                return ret
            ret+= f[i]

        return ret
