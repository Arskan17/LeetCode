# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        jj = []
        def pre(rut):
            if rut:
                jj.append(rut.val)
                pre(rut.left)
                pre(rut.right)
        pre(root)
        return jj

        