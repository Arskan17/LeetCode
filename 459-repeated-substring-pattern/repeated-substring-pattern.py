class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """The IDEA:
        If s is made of a repeating substring (e.g., $s = P + P$), what happens if you concatenate s with itself (s + s)
        ?You get P + P + P + P.
        If you remove the very first and very last characters of s + s, the original string s (P + P) will still appear somewhere inside that trimmed string. If s cannot be built by repeating P, s will not appear inside."""

        double_s = s+s
        trimed_double_s = double_s[1:-1]

        if s in trimed_double_s:
            return True

        return False