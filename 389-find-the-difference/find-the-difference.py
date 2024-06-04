class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # for i in t:
        #     if (i not in s): return i
        s = sorted(s)
        s.append(" ")
        t = sorted(t)

        for i in range(len(t)):
            if (s[i] != t[i]): return t[i]