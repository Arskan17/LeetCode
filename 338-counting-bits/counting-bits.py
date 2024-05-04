class Solution:
    def countBits(self, n: int) -> List[int]:
        # def countOnes(i):
        #     count = 0
        #     while i:
        #         i &= i - 1
        #         count += 1
        #     return count

        # return [countOnes(i) for i in range (n+1)]

        bits = [0] * (n+1)
        for i in range(n+1):
            bits[i] = bits[i >> 1] + (i & 1)
        return bits