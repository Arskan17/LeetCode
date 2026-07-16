class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        record = {0: -1}
        last_sum = 0

        for i, n in enumerate(nums):
            last_sum += n

            remainder = last_sum % k
            if remainder in record:
                if i - record[remainder] > 1:
                    return True

            else:
                record[remainder] = i

        return False
