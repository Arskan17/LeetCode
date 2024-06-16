class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # setOfNums1 = set(nums1)
        # setOfNums2 = set(nums2)
        return [commonNum for commonNum in set(nums1) if commonNum in set(nums2)]