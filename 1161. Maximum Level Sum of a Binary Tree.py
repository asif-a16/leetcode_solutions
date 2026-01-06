# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        queue = [root]
        cur_level = 1
        cur_max_sum = float('-inf')
        result = 1

        while queue:
            level_sum = 0
            next_level = []

            for node in queue:
                level_sum += node.val

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if level_sum > cur_max_sum:
                cur_max_sum = level_sum
                result = cur_level

            queue = next_level
            cur_level += 1

        return result
