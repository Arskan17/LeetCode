class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        record = {0: 1}
        running_sum = 0
        total_num_of_subarrays = 0

        for n in nums:
            running_sum += n

            # If (current sum - k) exists, we found a valid subarray
            target = running_sum - k
            if target in record:
                total_num_of_subarrays += record[target]

            if running_sum in record:
                record[running_sum] += 1
            else:
                record[running_sum] = 1
        
        return total_num_of_subarrays

