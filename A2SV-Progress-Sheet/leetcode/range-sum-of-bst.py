# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def rec(root, low, high):
            nonlocal ans
            if not root:
                return 
            if low <= root.val <= high:
                ans += root.val
            rec(root.left, low, high)
            rec(root.right, low, high)
        rec(root, low, high)
        return ans
