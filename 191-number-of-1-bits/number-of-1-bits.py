class Solution:
    def hammingWeight(self, n: int) -> int:
        number_of_one_bits = 0
        binary_value_of_n = format(n, 'b') # format() converts its first param depending on its second, in this case 'b' for binary

        for bit in binary_value_of_n:
            if int(bit) == 1:
                number_of_one_bits += 1

        return number_of_one_bits
        