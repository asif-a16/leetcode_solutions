# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        values = {p.val, q.val}

        def LCA(node):
            if not node:
                return -1
            
            left = LCA(node.left)
            right = LCA(node.right)

            if isinstance(left, TreeNode):
                return left
            if isinstance(right, TreeNode):
                return right
            
            if left in values and right in values and left != right:
                return node
            
            if left == p.val:
                if node.val == q.val:
                    return node
                else:
                    return left
            if right == p.val:
                if node.val == q.val:
                    return node
                else:
                    return right
                
            if left == q.val:
                if node.val == p.val:
                    return node
                else:
                    return left
            if right == q.val:
                if node.val == p.val:
                    return node
                else:
                    return right
                
            return node.val
        
        return LCA(root)
