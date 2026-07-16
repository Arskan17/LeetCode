class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        record = {}
        
        # 1. Build your dictionary exactly like your first approach
        for i, n in enumerate(nums):
            if n not in record:
                record[n] = []
            record[n].append(i)

        # Pre-fill the array so we can slot answers in out-of-order
        arr = [0] * len(nums)

        # 2. Iterate through the groups of indices
        for n, indices in record.items():
            
            # Start with all elements considered to be on the "right"
            right_sum = sum(indices)
            right_count = len(indices)
            left_sum = 0
            left_count = 0

            for i in indices:
                # Remove the current index from the right side pool
                right_sum -= i
                right_count -= 1

                # Calculate distances using the left/right counts and sums
                left_distance = (left_count * i) - left_sum
                right_distance = right_sum - (right_count * i)

                arr[i] = left_distance + right_distance

                # Add the current index to the left side pool for the next loop
                left_sum += i
                left_count += 1

        return arr