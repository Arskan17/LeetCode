class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        record = {0: 1}
        running_sum = 0
        subarray_sums_divisible_by_k = 0

        for n in nums:
            running_sum += n
            remainder = running_sum % k

            if remainder not in record:
                record[remainder] = 1
            else:
                subarray_sums_divisible_by_k += record[remainder]
                record[remainder] += 1


        return subarray_sums_divisible_by_k
