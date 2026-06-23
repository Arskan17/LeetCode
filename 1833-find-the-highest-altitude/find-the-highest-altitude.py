class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        rec = [0]
        for i in gain:
            t = rec[-1] + i
            rec.append(t)

        return max(rec)