# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        depths = defaultdict(list)
        queue.append((root, 0))

        while queue:
            node, level = queue.popleft()

            if not node:
                continue

            depths[level].append(node.val)

            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        return [depth[-1] for depth in depths.values()]
