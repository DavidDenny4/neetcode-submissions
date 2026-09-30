# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        visited = set()
        while curr:
            visited.add(curr)
            curr = curr.next
            if curr in visited:
                return False
        return True