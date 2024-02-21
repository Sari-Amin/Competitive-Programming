# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def rec(node, start = float("-inf"), end = float("inf")):
            
            if not node:
                return True
            if start >= node.val or node.val >= end:
                return False
            left = rec(node.left, start, node.val)
            right = rec(node.right, node.val, end)
            return left and right

        return rec(root)