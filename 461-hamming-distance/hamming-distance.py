class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = format(x, 'b')
        bin_y = format(y, 'b')
        longest_bin_str = max(len(bin_x), len(bin_y))

        tup = zip(bin_x.zfill(longest_bin_str), bin_y.zfill(longest_bin_str))
        return sum([1 for i, j in tup if i!=j])