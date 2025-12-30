# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0

        def helper(node, path_max):
            if not node:
                return 0
            
            if node.val >= path_max:
                self.good_nodes += 1
                path_max = node.val

            helper(node.left, path_max)
            helper(node.right, path_max)

        helper(root, root.val)
        
        return self.good_nodes
