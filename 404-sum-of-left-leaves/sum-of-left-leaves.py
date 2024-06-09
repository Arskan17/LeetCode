# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # leaveSum = 0

        def sumemL(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val

            return sumemL(root.left) + sumemR(root.right) 

        def sumemR(root):
            if not root:
                return 0
            
            return sumemL(root.left) + sumemR(root.right)

        return sumemL(root.left) + sumemR(root.right)
        