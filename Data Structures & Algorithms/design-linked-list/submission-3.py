class ListNode:

    def __init__(self, val = None):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        count = -1
        curr = self.head
        while curr != self.tail:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        newNode.prev = self.head
        newNode.next.prev = newNode
        self.head.next = newNode

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        newNode.prev.next = newNode
        self.tail.prev = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        count = -1
        curr = self.head
        while curr.next:
            if count == index - 1:
                newNode = ListNode(val)
                newNode.next = curr.next
                newNode.prev = curr
                curr.next.prev = newNode
                curr.next = newNode
            curr = curr.next


    def deleteAtIndex(self, index: int) -> None:
        count = -1
        curr = self.head
        while curr.next:
            if count == index - 1:
                curr.next.next.prev = curr
                curr.next = curr.next.next
            curr = curr.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)