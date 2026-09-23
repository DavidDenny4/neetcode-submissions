class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        count = 0
        while curr:
            if count == index:
                return curr.value
            count += 1
            curr = curr.next

        return -1
            
    def insertHead(self, val: int) -> None:
        new_head = Node(val)
        new_head.next = self.head.next
        self.head.next = new_head
        if new_head.next is None:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        new_tail = Node(val)
        self.tail.next = new_tail
        self.tail = new_tail

    def remove(self, index: int) -> bool:
        curr = self.head
        count = 0
        while curr and count < index:
            count += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
            

    def getValues(self) -> List[int]:
        result = []
        curr = self.head.next
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result
