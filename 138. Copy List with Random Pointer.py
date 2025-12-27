"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        nodes = {}
        def createNode(node: 'Optional[Node]') -> 'Optional[Node]':
            if node.next == None:
                nodes[node.next] = None
            if node.next not in nodes:
                createNode(node.next)
            new_node = Node(node.val, nodes[node.next])
            nodes[node] = new_node
            return new_node
        
        new_head = createNode(head)
        current = new_head

        while current:
            current.random = nodes[head.random]
            current = current.next
            head = head.next

        return new_head
