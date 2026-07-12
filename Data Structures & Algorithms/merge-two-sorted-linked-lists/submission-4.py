# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(-1)
        head = result
        curr, curr2 = list1, list2
        while curr and curr2:
            if curr.val < curr2.val:
                result.next = curr
                curr = curr.next
            else:
                result.next = curr2
                curr2 = curr2.next
            result = result.next
        
        if curr:
            result.next = curr
        
        if curr2:
            result.next = curr2
        
        return head.next
        
