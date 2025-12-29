# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def maxDepth(node: TreeNode):
            if not node: return 0
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            if node.left and not left or node.right and not right:
                return False
            if abs(left - right) > 1:
                return False
            return max(left, right) + 1
        
        return bool(maxDepth(root))
