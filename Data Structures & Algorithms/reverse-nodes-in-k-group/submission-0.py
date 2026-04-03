# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        nodes = 0
        while cur:
            nodes += 1
            cur = cur.next

        reversetimes = nodes // k
        dummy = ListNode(0, head)
        prev = dummy
        nxt = head
        for i in range(reversetimes):
            start = prev.next
            curr = prev.next
            jprev = None
            for j in range(k):
                nxt = curr.next
                curr.next = jprev
                jprev = curr
                curr = nxt

            prev.next = jprev   #prev point to new head
            start.next = nxt    #tail point to old next
            prev = start        #update prev to new tail before

        return dummy.next     
