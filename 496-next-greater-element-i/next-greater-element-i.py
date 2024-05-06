class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if (nums1[i] == nums2[j]):
                    if (j+1==len(nums2)):
                        arr.append(-1)
                        break
                    m = 0
                    for h in range(j+1, len(nums2)):
                        if (nums2[h] > nums2[j]):
                            m = nums2[h]
                            break
                        else: m = -1
                    arr.append(m)
        return arr