# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def treeMax(rut):
            if not rut:
                return 0
            if not rut.left: return 1 + treeMax(rut.right)
            if not rut.right: return 1 + treeMax(rut.left)
            return 1+ min(treeMax(rut.left), treeMax(rut.right))
        return treeMax(root)