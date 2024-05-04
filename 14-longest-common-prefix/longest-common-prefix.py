class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = []
        for n in range(len(min(strs))):
            c=[]
            for i in range(len(strs)):
                c.append(strs[i][n])
            if all(x == c[0] for x in c):
                pref.append(c[0])
            else: break
        return ''.join(pref)