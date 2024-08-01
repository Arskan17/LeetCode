# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None  # Handles empty list

        # Checks if the first element needs removal
        if head.val == val:
            return self.removeElements(head.next, val)  # Recursively remove from the rest

        # Set head correctly by pointing to the modified sublist (if any)
        head.next = self.removeElements(head.next, val)
        return head
        
        