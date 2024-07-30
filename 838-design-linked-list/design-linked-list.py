class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        head = self.head

        if (index == 0) and (not head): # handles case where list is empty
            return -1

        for _ in range(index):
            if not head.next: # handles case where the index is invalid (out of bounds)
                return -1
            
            head = head.next

        return head.val


    def addAtHead(self, val: int) -> None:
        node = Node(val)

        if not self.head: # handles case where list is empty
            self.head = node
            return
            
        node.next = self.head
        self.head = node
        

    def addAtTail(self, val: int) -> None:
        node = Node(val) # initialize the value

        # if list empty, initialize the list with the new node
        if not self.head:
            self.head = node
            return

        # if list not empty, itterate till the end of the list, and point the end's next to the new node
        head = self.head
        while head.next:
            head = head.next

        head.next = node
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val) # initialize the value

        head = self.head

        if (index == 0) and (not head): # handles case where list is empty, but we wanna add at the beginning
            self.head = node
            return

        if (index > 0) and (not head): # handles case where list is empty, but we wanna add at a position other than the first
            return

        if (index == 0) and (not head.next): # handles case where we wanna add at the beginning
            node.next = head
            self.head = node

        for _ in range(index-1):
            if not head.next: # handles case where the index is invalid (out of bounds)
                return

            head = head.next

        if not head.next: # handles case where we're adding at the end of the list
            head.next = node
            return

        node.next = head.next
        head.next = node
        

    def deleteAtIndex(self, index: int) -> None:
        head = self.head

        if not head: # handles case where list is empty
            return

        # handles case where we wanna delete element at the beginning of the list.
        if (index == 0) and (head.next):
            self.head = head.next
            return

        # handles case where we wanna delete element at the beginning of the list, and the list only has one elemet
        if (index == 0) and (not head.next):
            self.head = None
            return

        for _ in range(index-1):
            if not head.next: # handles case where the index is invalid (out of bounds)
                return

            head = head.next

        if not head.next:
            head = None            
            return
            
        if not (head.next).next:
            head.next = None
            return

        nextNode = (head.next).next
        head.next = nextNode
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)