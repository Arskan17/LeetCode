class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        def find_duplicate(lst):
            counts = Counter(lst)
            duplicate = [item for item, count in counts.items() if count > 1]
            return duplicate[0]

        def find_missing(lst, n):
            expected_sum = n * (n + 1) // 2
            actual_sum = sum(lst) - find_duplicate(lst)
            return expected_sum - actual_sum

        return[find_duplicate(nums),find_missing(nums, len(nums))]
