class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        setOfNum1 = set(nums1)
        setOfNum2 = set(nums2)
        return [commonNum for commonNum in setOfNum1 if commonNum in setOfNum2]