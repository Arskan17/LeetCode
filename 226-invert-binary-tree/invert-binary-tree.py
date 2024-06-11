# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inverseMeThis(root):
            if not root:
                return root
            tempLeftTree = inverseMeThis(root.left)
            root.left = inverseMeThis(root.right)
            root.right = tempLeftTree
            return root
        
        return inverseMeThis(root)