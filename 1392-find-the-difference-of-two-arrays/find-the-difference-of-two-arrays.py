class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer0 = [num for num in nums1 if num not in nums2]
        answer1 = [num for num in nums2 if num not in nums1]
        return [set(answer0), set(answer1)]