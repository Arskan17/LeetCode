class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        jj = [j for i in range(len(nums1)) for j in range(len(nums2)) if nums1[i] == nums2[j]]

        for k in jj:
            if (k >= len(nums2)): arr.append(-1)
            else:
                m = -1
                for h in range(k, len(nums2)):
                    if (nums2[h] > nums2[k]):
                        m = nums2[h]
                        break
                arr.append(m)
        return arr