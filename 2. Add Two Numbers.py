# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = 0
        multiplier = 1

        cur1 = l1
        cur2 = l2
        while cur1 and cur2:
            result += (cur1.val + cur2.val) * multiplier
            multiplier *= 10
            cur1 = cur1.next
            cur2 = cur2.next

        while cur1:
            result += cur1.val * multiplier
            multiplier *= 10
            cur1 = cur1.next

        while cur2:
            result += cur2.val * multiplier
            multiplier *= 10
            cur2 = cur2.next
        
        result = f"{result}"
        summ = ListNode(0)
        cur = summ

        for i in range(len(result) - 1, -1, -1):
            cur.next = ListNode(int(result[i]))
            cur = cur.next

        return summ.next
