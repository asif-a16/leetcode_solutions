# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = deque()

        while head:
            nodes.append(head)
            head = head.next

        while nodes:
            if len(nodes) >= 2:
                left = nodes.popleft()
                left.next = nodes[-1]
                right = nodes.pop()
                right.next = nodes[0] if nodes else None
                continue
            if nodes:
                remaining = nodes.pop()
                remaining.next = None
