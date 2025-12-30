# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result = defaultdict(list)
        queue.append((root, 0))

        while queue:
            node, level = queue.popleft()
            if not node:
                continue
            
            result[level].append(node.val)

            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        return list(result.values())
