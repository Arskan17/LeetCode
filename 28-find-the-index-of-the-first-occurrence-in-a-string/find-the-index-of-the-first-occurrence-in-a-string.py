class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # base case when needle is empty
        if not needle:
            return 0
        l = len(needle)
        # checks if needle is in stack
        for i in range(len(haystack) - l + 1):
            if haystack[i:i+l] == needle:
                return i
        return -1