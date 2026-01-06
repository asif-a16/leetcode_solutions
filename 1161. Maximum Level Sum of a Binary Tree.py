# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution(object):
    def maxLevelSum(self, root):
        queue = deque([(root, 1)])
        level_sums = defaultdict(int)
        result = 1
        cur_max_sum = float("-inf")

        while queue:
            node, level = queue.popleft()
            if not node:
                continue

            level_sums[level] += node.val

            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        
        for level, level_sum in level_sums.items():
            if level_sum > cur_max_sum:
                cur_max_sum = level_sum
                result = level
                
        return result
