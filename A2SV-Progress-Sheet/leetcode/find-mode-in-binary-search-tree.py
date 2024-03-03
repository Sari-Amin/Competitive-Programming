# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = {}

        def dfs(root):
          
            if not root:
                return 
            dic[root.val] = dic.get(root.val, 0) + 1
            
            dfs(root.left)
            dfs(root.right)
       
        dfs(root)
        max_ = max(dic.values())
        return [num for num in dic if dic[num] == max_]
