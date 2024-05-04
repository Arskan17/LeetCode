class Solution:
    def romanToInt(self, s: str) -> int:
        keyVal = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        tot = 0
        for i in range(len(s)):
            if((keyVal[s[i]] <= keyVal[s[i-1]]) or i==0):
                tot += keyVal[s[i]]
            elif (keyVal[s[i]] > keyVal[s[i-1]]):
                tot += keyVal[s[i]] - keyVal[s[i-1]]*2
        return tot