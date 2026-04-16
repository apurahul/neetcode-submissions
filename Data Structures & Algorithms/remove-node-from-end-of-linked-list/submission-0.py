# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # 2 pass method
        #find the number of nodes

        # N = 0
        # curr = head
        # while curr:
        #     N += 1
        #     curr = curr.next
        
        # remove_index = N - n

        # if remove_index == 0:
        #     return head.next

        # curr = head
        # for i in range(N - 1):
    
        #     if i == remove_index - 1:
        #         curr.next = curr.next.next
        #         break

        #     curr = curr.next
        
        # return head


        #2 pointer approach


        #create a 2 pointer which are n distanec apart and keep moving them one sep till you reach the last step


        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next

        