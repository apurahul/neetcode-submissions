# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # def rec(self, head, n):
    #     if not head:
    #         return None
        
    #     head.next = self.rec(head.next, n)
    #     n[0] -= 1
    #     if n[0] == 0:
    #         return head.next
    #     return head


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     return self.rec(head, [n])

    #simpler way - use  pointers
    # 2poiters with distance of n between then an then move them one step ata time, when the last pne reaches the end, the ifirst one is on nth positin then do next.next

        dummy = ListNode(0, head)

        left, right= dummy, head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next




        