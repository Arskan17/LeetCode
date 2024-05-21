# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''WHY EXACTLY DOES THE TEST PASSES EVEN THOUGH i DIDN'T DO ANYTHING YET???????'''
        # lst
        # def sss(rut):
        #     if rut:
        #         sss(rut.left)
        #         lst.append(rut.val)
        #         sss(rut.right)

        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)

        if not root:  # Handle empty tree case
            return True
        return isMirror(root.left, root.right)
        