# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # break the list into 2 using floyds algortihem oif slo and fast pointerss

        slow = fast = head
        l1 =  head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

 
        second = slow.next
        slow.next = None

        #reverse the second part

        curr = second
        p = None
    

        while curr:
            t = curr.next
            curr.next = p
            p = curr
            curr = t

        l2 = p


        #merge the 2 lists


        while l1 and l2:
            t1 = l1.next
            t2 = l2.next

            l1.next = l2
            l2.next = t1

            l1 = t1
            l2 = t2

            



