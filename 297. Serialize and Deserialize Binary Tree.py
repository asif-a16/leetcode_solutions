# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "n"

        result = []
        stack = [root]

        while stack:
            node = stack.pop()

            if node is None:
                result.append("n")
                continue

            result.append(str(node.val))

            stack.append(node.right)
            stack.append(node.left)

        return ",".join(result)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = deque(data.split(","))
        if not data or data[0] == "n":
            return None

        root = TreeNode(int(data.popleft()))
        stack = [(root, "left")]  # (node, next_child_to_fill)

        while data:
            val = data.popleft()
            node, state = stack[-1]

            if state == "left":
                if val == "n":
                    node.left = None
                    stack[-1] = (node, "right")
                else:
                    new_node = TreeNode(int(val))
                    node.left = new_node
                    stack[-1] = (node, "right")
                    stack.append((new_node, "left"))

            else:  # state == "right"
                if val == "n":
                    node.right = None
                    stack.pop()
                else:
                    new_node = TreeNode(int(val))
                    node.right = new_node
                    stack.pop()
                    stack.append((new_node, "left"))

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))