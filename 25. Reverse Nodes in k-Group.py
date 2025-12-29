# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = head
        right = head
        
        for _ in range(k - 1):
            right = right.next
        
        new_head = right
        prev_tail = None

        while right:
            new_prev_tail = left
            prev = None
            for _ in range(k):
                nxt = left.next
                left.next = prev
                prev = left
                left = nxt

                if right: right = right.next

            if prev_tail:
                prev_tail.next = prev

            prev_tail = new_prev_tail

        prev_tail.next = left

        return new_head
