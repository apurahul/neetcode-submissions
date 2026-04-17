class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # arr = []
        # for row in matrix:
        #     for i in row:
        #         arr.append(i)

        # l = 0
        # r = len(arr) -1

        # while l <= r:
        #     m = l + ((r - l) // 2)

        #     if arr[m] == target:
        #         return True
        #     elif arr[m] > target :
        #         r = m - 1
        #     else:
        #         l = m + 1
        # return False


        # the above logic takes O(m*n) extra space

        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1

        while l <= r:
            m = l + ((r - l) //2)
            r_i = m // cols
            c_i = m % cols
            val = matrix[r_i][c_i]

            if val == target:
                return True
            elif val > target:
                r = m - 1
            else:
                l = m + 1
        
        return False
                

