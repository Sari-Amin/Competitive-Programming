# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        if root == None:
            return 0
        self.rec(root,root.val,root.val)
        return self.ans
    def rec(self,root,minm,maxm):
        if root == None:
            return
        self.ans = max(self.ans,abs(minm-root.val),abs(maxm-root.val))
        minm = min(minm, root.val)
        maxm = max(maxm, root.val)
        self.rec(root.left, minm, maxm)
        self.rec(root.right, minm, maxm)