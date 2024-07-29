# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binNumber = ""

        # get all the digits from the linked-list into a string
        while head:
            binNumber += str(head.val)
            head = head.next

        # then traverse the list in reverse order and multiply every digit by two to the power of its position in the string
        # it's the same as doing `int(binNumber, 2)`, but uses less memory
        decNumber = 0
        for i, digit in enumerate(binNumber[::-1]):
            decNumber += int(digit) * (2**i)

        return decNumber