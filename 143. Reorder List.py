from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
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

            nodes.pop().next = None
