class Solution:
    
    def concatenatedBinary(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
            
        binary_string = ""

        for i in range(1, n+1):
            binary_string += bin(i)[2:]

        return int(binary_string, 2) % ((10**9) + 7)
        