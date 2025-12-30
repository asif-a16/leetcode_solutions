# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedList
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        
        def dfs(node):
            if not node:
                return
            values.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        values.sort()

        return values[k-1]
