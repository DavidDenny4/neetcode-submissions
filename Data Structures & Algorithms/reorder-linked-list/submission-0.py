# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        # find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        
        # Reverse second list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        front = head
        second = prev

        while second:
            second_next = second.next
            front_next = front.next
            front.next = second
            second.next = front_next
            
            second = second_next
            front = front_next

            
        
