# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = float("-inf")

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            node_max = node.val
            if node.val + left > right + node.val and node.val + left > node.val:
                node_max = node.val + left
            elif right + node.val > node.val + left and node.val + right > node.val:
                node_max = node.val + right

            self.max = max(self.max, node_max, node.val + left + right)

            return node_max
        
        dfs(root)

        return self.max
