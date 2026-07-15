# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        num_lists = len(lists)
        dummy = ListNode()
        curr = dummy
        while num_lists > 0:
            # find min node in lists and which index from the list
            min_val = float(inf)
            min_index = 0
            for i in range(num_lists):
                if lists[i].val < min_val:
                    min_val = lists[i].val
                    min_index = i
            
            min_node = lists[min_index]
            min_next = min_node.next
            curr.next = min_node
            min_node = min_next

            if min_node is None:
                lists.remove(min_index)
            
            curr = curr.next

        return dummy.next
                
            