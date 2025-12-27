class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        current = head

        while current:
            nodes.append(current)
            current = current.next

        if len(nodes) - n == 0:
            return head.next
        
        nodes[len(nodes) - n - 1].next = nodes[len(nodes) - n + 1] if n > 1 else None

        return head
