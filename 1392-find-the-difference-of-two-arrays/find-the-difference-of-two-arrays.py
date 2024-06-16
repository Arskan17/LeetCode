class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        setOfNum1, setOfNum2 = set(nums1), set(nums2)
        answer0 = [num for num in setOfNum1 if num not in setOfNum2]
        answer1 = [num for num in setOfNum2 if num not in setOfNum1]
        return [answer0, answer1]