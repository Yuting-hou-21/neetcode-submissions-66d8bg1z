# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next #slow: 0->1->2... fast: 1->3->5...

        # find mid (slow.next)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondhalf = slow.next
        prev = slow.next = None

        # reverse the second half
        while secondhalf:
            tmp = secondhalf.next
            secondhalf.next = prev
            prev = secondhalf
            secondhalf = tmp

        # mix
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        
