# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def maxDepth(node):
            if not node: 
                return 0
            
            max_left = maxDepth(node.left)
            max_right = maxDepth(node.right)
            self.diameter = max(self.diameter, max_left + max_right)
            
            return max(max_left, max_right) + 1
        
        maxDepth(root)

        return self.diameter
