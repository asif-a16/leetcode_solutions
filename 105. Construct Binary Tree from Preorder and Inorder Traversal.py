# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def buildTree(self, preorder, inorder):
        preorder = deque(preorder)
        inorder = deque(inorder)

        root = TreeNode(preorder.popleft())
        stack = [root]
        cur = root

        while preorder:
            if cur.val != inorder[0]:
                # build left subtree
                cur.left = TreeNode(preorder.popleft())
                stack.append(cur.left)
                cur = cur.left
            else:
                # unwind stack to find parent for right child
                while stack and stack[-1].val == inorder[0]:
                    cur = stack.pop()
                    inorder.popleft()

                # build right subtree if preorder remains
                if preorder:
                    cur.right = TreeNode(preorder.popleft())
                    stack.append(cur.right)
                    cur = cur.right

        return root
