# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        list_empty = False
        nodes = {}

        for idx, node in enumerate(lists):
            nodes[idx] = node

        while not list_empty:
            cur_min = float("inf")
            min_head_idx = None
            list_empty = True

            for i in range(len(nodes)):
                head = nodes[i]
                if head and head.val < cur_min:
                    list_empty = False
                    cur_min = head.val
                    min_head_idx = i

            if list_empty: break
            cur.next = ListNode(cur_min)
            cur = cur.next
            nodes[min_head_idx] = nodes[min_head_idx].next

        return dummy.next
