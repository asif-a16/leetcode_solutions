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
        queue = deque([root])
        builder = []
        cur = root
        while queue:
            node = queue.popleft()

            if not node:
                builder.append("-#")
                continue

            builder.append(f"{node.val}#")
            queue.append(node.left)
            queue.append(node.right)

        return "".join(builder)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        data = deque(data)
        builder = []
        node_vals = deque()
        while data:
            while data[0] != "#":
                builder.append(data.popleft())

            data.popleft()

            value = "".join(builder)

            if value == "-":
                node_vals.append(None)
            else:
                node_vals.append(int(value))

            builder = []

        root = TreeNode(node_vals.popleft())
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                continue

            if node_vals:
                if node_vals[0] != None:
                    node.left = TreeNode(node_vals.popleft())
                else:
                    node_vals.popleft()
                    
            if node_vals:
                if node_vals[0] != None:
                    node.right = TreeNode(node_vals.popleft())
                else:
                    node_vals.popleft()

            queue.append(node.left)
            queue.append(node.right)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))