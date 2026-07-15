# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        # Handle empty list
        if not head:
            newNode = Node(insertVal)
            newNode.next = newNode
            return newNode
        
        # Case 1: 1 Node
        if head.next == head:
            newNode = Node(insertVal)
            newNode.next = head
            head.next = newNode
            return newNode if newNode.val < head.val else head

        # Case 2: 2+ Nodes
        curr = head
        curr_next = curr.next
        newNode = Node(insertVal)
        while True:
            if curr.val > curr_next.val and (newNode.val > curr.val or newNode.val < curr_next.val):
                curr.next = newNode
                newNode.next = curr_next
                return head
            if newNode.val >= curr.val and newNode.val <= curr_next.val:
                curr.next = newNode
                newNode.next = curr_next
                return head
            curr = curr.next
            if curr == head:
                break
        
        return head
            
