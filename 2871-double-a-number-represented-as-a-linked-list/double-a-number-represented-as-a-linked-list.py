# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        tmp = head
        # reverse the list the first time
        while tmp:
            nxt = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = nxt
        # return tmp
        
        prv = None
        carry = 0
        # then re-reverse it while multiplying by 2 and adding the carry
        while prev:
            nxt = prev.next
            digit_value = prev.val * 2 + carry  # Extract digit value, double, and add carry
            carry, digit = divmod(digit_value, 10)  # Separate carry and digit (efficient)
            new_node = ListNode(digit)  # Create a new node with the resulting digit
            new_node.next = prv
            prv = new_node
            prev = nxt
        
        # Handle the case where the result is a single digit (carry > 0)
        if carry > 0:
            new_node = ListNode(carry)
            new_node.next = prv
            prv = new_node

        return prv


        