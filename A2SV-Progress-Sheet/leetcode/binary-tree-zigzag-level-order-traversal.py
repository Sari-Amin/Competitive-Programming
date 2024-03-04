# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        def dfs(root, depth = 0):
            if not root:
                return
            
            dic[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)


        dfs(root)
        ans = []
        for i in dic:
            if i % 2:
                ans.append(dic[i][::-1])
                continue
            ans.append(dic[i])
            
        return ans