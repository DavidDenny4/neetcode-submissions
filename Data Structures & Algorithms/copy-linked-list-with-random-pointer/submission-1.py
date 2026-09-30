"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        new_map = {}

        while curr:
            newNode = Node(curr.val)
            new_map[curr] = newNode
            curr = curr.next

        curr = head
        while curr:
            if curr.next is not None:
                new_map[curr].next = new_map[curr.next]
            else:
                new_map[curr].next = None
            if curr.random is not None:
                new_map[curr].random = new_map[curr.random]
            else:
                new_map[curr].random = None
            curr = curr.next
        return new_map[head]
