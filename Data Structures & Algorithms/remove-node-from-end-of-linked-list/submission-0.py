# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = head, head
        i = n
        prev = None
        while second:
            second = second.next
            i -= 1
            if second == None:
                if prev == None:
                    head = head.next
                else:
                    prev.next = first.next
            if i <= 0:
                prev = first
                first = first.next


        return head