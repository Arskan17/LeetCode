# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # tree = TreeNode(None)

        def constructTree(nums, leftIndex, rightIndex):
            if leftIndex > rightIndex: return None

            mid = (leftIndex + rightIndex) // 2
            tree = TreeNode(nums[mid])
            tree.left = constructTree(nums, leftIndex, mid-1)
            tree.right = constructTree(nums, mid+1, rightIndex)
            return tree
            

        return constructTree(nums, 0, len(nums)-1)

        # return tree
        