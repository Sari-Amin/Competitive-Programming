# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(root, sm = ""):
            nonlocal ans
            if not root:
                return 
            if not root.left and not root.right:
                ans += int(sm + str(root.val))
            sm += str(root.val)
            dfs(root.left, sm)
            dfs(root.right, sm)
        
        dfs(root)
        return ans