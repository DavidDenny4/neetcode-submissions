class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)

    def get(self, index: int) -> int:
        curr = self.head.next
        count = 0
        while curr:
            count += 1
            if count == index:
                return curr.value
            curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode

    def addAtTail(self, val: int) -> None:
        curr = self.head.next
        while curr:
            curr = curr.next
        
        newNode = Node(val)
        curr.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        curr = self.head.next
        count = 0
        while curr and count < index:
            curr = curr.next
            count += 1

        newNode.next = curr.next
        curr.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        count = 0
        while curr and count < index:
            curr = curr.next
            count += 1
        
        curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)