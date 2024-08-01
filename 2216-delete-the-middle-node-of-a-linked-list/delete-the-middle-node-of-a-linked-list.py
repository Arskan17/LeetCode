# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Get the list's length first
        length = 0
        getlength = head
        while getlength:
            length += 1
            getlength = getlength.next

        if length == 1 or length == 0: # handles case where list only has one node, or no nodes at all
            head = None
            return head

        if length == 2: # handles case where the middle is the end of the list, ie the list only has 2 nodes.
            head.next = None
            return head

        # get to the node b4 the middle
        length = length//2
        rest = head # copy the list
        head = rest # and make the head point to that, since we'll need it to go to the middle
        for _ in range(length-1):
            rest = rest.next

        rest.next = (rest.next).next

        return head
