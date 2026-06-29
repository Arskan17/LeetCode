class Solution:
    def reverseBits(self, n: int) -> int:
        """
        - format(n, '032b'): Converts the number to a 32-character wide binary string, padding with leading zeros.

        - [::-1]: Reverses the string.

        - int(..., 2): Parses the binary string back into a base-10 integer.
        """
        return int(format(n, '032b')[::-1], 2)
