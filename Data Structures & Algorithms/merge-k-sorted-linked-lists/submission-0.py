# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, node1, node2) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while node1 and node2:
            if node1.val < node2.val:
                tail.next = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2 = node2.next
            
            tail = tail.next

        if node1:
            tail.next = node1
        elif node2:
            tail.next = node2

        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = len(lists)
        for i in range(1,nodes):
            lists[i] = self.mergeTwoLists(lists[i], lists[i - 1])

        return lists[nodes - 1] if nodes - 1 > 0 else None