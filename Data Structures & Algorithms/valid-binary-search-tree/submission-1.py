# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # def isValid(root, low, high):
            
        #     if not root:
        #         return True

        #     if not (low < root.val <high):
        #         return False
            
        #     return isValid(root.left, low, root.val) and isValid(root.right, root.val, high)



        # return isValid(root, float('-inf'), float('inf'))
        

        # how to do it with ietration?
        # checking each node but we need to store, do we can do bfs with iteration

        if not root:
            return True

        q = deque([(root, float('-inf'), float('inf'))])

        while q:
            node, low, high = q.popleft()

            if not (low < node.val < high):
                return False
            else: 
                if node.left:
                    q.append((node.left, low, node.val))
                    
                if node.right:
                        q.append((node.right, node.val, high))

        return True
