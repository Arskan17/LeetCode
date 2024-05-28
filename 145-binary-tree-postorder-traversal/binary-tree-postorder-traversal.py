# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        jj = []
        def post(rut):
            if rut:
                post(rut.left)
                post(rut.right)
                jj.append(rut.val)
        post(root)
        return jj
        