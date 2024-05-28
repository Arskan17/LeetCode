# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        jj = head
        while jj and jj.next:
            head = head.next
            jj = jj.next.next
            # jj = jj.next
            if head is jj:
                return True

        return False