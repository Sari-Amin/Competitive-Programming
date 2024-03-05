# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        #if one is the ancestor of the other
        if root.val == p.val or root.val == q.val:
            return root

        #if one is in left subtree and the other in right subtree 
        if q.val > root.val and p.val < root.val or q.val < root.val and p.val > root.val:
            return root

        #if both are in the left subtree
        if q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
            
        #if both are in the right subtree
        return self.lowestCommonAncestor(root.right,p,q)
        