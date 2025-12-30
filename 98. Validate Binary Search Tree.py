# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return (True, float("inf"), float("-inf"))
            
            if not node.left and not node.right:
                return (True, node.val, node.val)
            
            is_valid_left, min_val_left, max_val_left = dfs(node.left)
            is_valid_right, min_val_right, max_val_right = dfs(node.right)

            if not is_valid_left or not is_valid_right:
                return (False, float("inf"), float("-inf"))
            
            is_valid = True

            if min_val_right <= node.val:
                is_valid = False
                
            if max_val_left >= node.val:
                is_valid = False
            
            min_left = min(min_val_left, min_val_right, node.val)
            max_right = max(max_val_left, max_val_right, node.val)

            return (is_valid, min_left, max_right)

        return dfs(root)[0]
