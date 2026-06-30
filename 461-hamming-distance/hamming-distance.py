class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """Slightly better version"""
        # 1. Find the max bit length needed
        max_len = max(x, y).bit_length()
        
        # 2. Find the next power of 2 padding size (default to 1 if max_len is 0)
        pad_to = 1 << (max_len - 1).bit_length() if max_len > 0 else 1
        
        # 3. Format with the power-of-2 padding
        bin_x = format(x, f'0{pad_to}b')
        bin_y = format(y, f'0{pad_to}b')
        
        # Count the mismatches
        return sum(1 for i, j in zip(bin_x, bin_y) if i != j)