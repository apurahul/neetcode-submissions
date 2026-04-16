# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = list3 = ListNode()

        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                list3.next = curr1
                curr1 = curr1.next
        
            else:
                list3.next = curr2
                curr2 = curr2.next

            list3 = list3.next

        list3.next = curr1 or curr2


        
        return dummy.next
        