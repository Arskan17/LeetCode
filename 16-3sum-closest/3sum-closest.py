class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # jj = [[i,j] for i in range(len(nums)-2) for j in range(len(nums)-1)]
        # tmp = [[jj[i[0]], jj[i[1]], j] for i in range(len(jj)) for j in range(jj[i[1]]+1, len(nums))]
        # tmp_nums = [[i[0], i[1], i[2]] for i in tmp]
        # smm = [sum(t) for t in tmp_nums]
        # smmm = [abs(target - i) for i in smm]
        
        # return min (smmm)

          # Sort the list for efficient two-pointer approach
        nums.sort()

        # Handle cases where there are less than 3 elements or all elements are the same
        if len(nums) < 3 or (len(nums) > 2 and nums[0] == nums[-1]):
            return sum(nums[:3])  # Return sum of first 3 elements (or all if same)

        closest_sum = float('inf')
        for i in range(len(nums) - 2):
            # Skip duplicates (don't consider the same element as the first element in the triplet)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                diff = abs(target - current_sum)

                # Update closest sum and pointers if a closer triplet is found
                if diff < closest_sum:
                    closest_sum = diff
                    closest_triplet = [nums[i], nums[left], nums[right]]  # Track the closest triplet

                # Early termination for perfect match or zero difference
                if current_sum == target or diff == 0:
                    return sum(closest_triplet)

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1

        # Return the sum of the closest triplet elements
        return sum(closest_triplet)