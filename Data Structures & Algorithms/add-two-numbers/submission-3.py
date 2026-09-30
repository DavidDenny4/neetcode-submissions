# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = None
        dummyNode = ListNode(-1)
        curr = dummyNode

        while l1 or l2 or carry:
            l1_val = l1.val if l1.val else 0
            l2_val = l2.val if l2.val else 0
            carry = carry if carry else 0

            sum = l1_val.val + l2.l2_val + carry
            carry = sum // 10 
            newNode = ListNode(sum)
            curr.next = newNode
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummyNode.next

        
