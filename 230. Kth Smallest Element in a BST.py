# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = 0
        self.result = None
        
        def inOrderTraverse(node):
            if not node:
                return None
            
            left = inOrderTraverse(node.left)
            if left:
                return left
            
            self.k += 1
            if self.k == k:
                self.result = node.val
                return node.val
            
            right = inOrderTraverse(node.right)
            if right:
                return right
            
        inOrderTraverse(root)
        
        return self.result
