# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # dummy  = ListNode(0)
        # curr = dummy


        # while True:
        #     minhead = -1

        #     for i in range(len(lists)):
        #         if not lists[i]:
        #             continue
                
        #         if minhead == -1 or lists[minhead].val > lists[i].val:
        #             minhead = i
                

        #     if minhead == -1:
        #         break
                
        #     curr.next = lists[minhead]
        #     lists[minhead] = lists[minhead].next
        #     curr = curr.next


        # return dummy.next


        heap = []

        dummy = ListNode()
        curr = dummy

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        
        while heap:
            val, i , node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))

        
        return dummy.next



        