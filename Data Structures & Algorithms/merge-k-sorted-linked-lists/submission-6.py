# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        num_lists = len(lists)
        print(num_lists)
        dummy = ListNode()
        curr = dummy
        while len(lists) > 0:
            # find min node in lists and which index from the list
            min_val = float('inf')
            min_index = 0
            for i in range(len(lists)):
                if lists[i].val is not None and lists[i].val < min_val:
                    min_val = lists[i].val
                    min_index = i
            
            min_node = lists[min_index]
            min_next = min_node.next
            curr.next = min_node
            lists[min_index] = lists[min_index].next

            if min_node is None:
                lists.pop(min_index)
            
            curr = curr.next

        return dummy.next
                
            