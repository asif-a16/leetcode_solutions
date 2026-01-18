"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        created_nodes = {}
        stack = [node]

        while stack:
            cur_node = stack.pop()
            node_copy = created_nodes.get(cur_node.val, Node(cur_node.val))

            for neighbour in cur_node.neighbors:
                if neighbour.val not in created_nodes:
                    stack.append(neighbour)
                    new_neighbour_node = Node(neighbour.val)
                    created_nodes[neighbour.val] = new_neighbour_node
                node_copy.neighbors.append(created_nodes[neighbour.val])

            if cur_node.val not in created_nodes:
                created_nodes[cur_node.val] = node_copy

        return created_nodes[1]
