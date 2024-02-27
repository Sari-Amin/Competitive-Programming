# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def rec(root):
            nonlocal ans

            if not root:
                return -1

            left = rec(root.left) + 1
            right = rec(root.right) + 1

            ans = max(ans, left + right, right, left)
            return max(left, right)
        rec(root)
        return ans
