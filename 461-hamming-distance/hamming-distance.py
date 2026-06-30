class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """Easiest best version"""
        # This skips string conversion entirely
        # It uses the XOR operator (^), which inherently compares bits, and then count the 1s
        return bin(x ^ y).count('1')