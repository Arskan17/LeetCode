class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set([commonNum for commonNum in nums1 if commonNum in nums2])