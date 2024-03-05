# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(l,r):

            if r < l:
                return
            
            max_ = float("-inf")
            index = l
            for i in range(l,r + 1):
                if nums[i] > max_:
                    max_ = nums[i]
                    index = i

            Node = TreeNode(max_)
            Node.left = dfs(l, index - 1)
            Node.right = dfs(index + 1, r)
            return Node

        return dfs(0, len(nums) - 1)
         