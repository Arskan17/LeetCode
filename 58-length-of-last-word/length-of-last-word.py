class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = 0
        prev = 0
        for i in range(len(s)):
            if s[i] == " " and s[i-1] != " ":
                prev = n
                n = 0
            elif s[i] == " ": n = 0
            else: n+=1
        if n == 0: return prev
        return n