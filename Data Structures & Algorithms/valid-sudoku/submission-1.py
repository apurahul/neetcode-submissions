class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # for row in range(9):
        #     seen = set()

        #     for i in range(9):
        #         if board[row][i] == ".":
        #             continue
        #         elif board[row][i] in seen:
        #             return False
        #         else:
        #             seen.add(board[row][i])

        # for col in range(9):
        #     seen = set()

        #     for i in range(9):
        #         if board[i][col] == ".":
        #             continue
        #         if board[i][col] in seen:
        #             return False

        #         seen.add(board[i][col])


        # for sqaure in range(9):
        #     seen = set()

        #     for i in range(3):
        #         for j in range(3):
        #             row = (sqaure//3) * 3 + i
        #             col = (sqaure % 3) * 3 + j

        #             if board[row][col] == ".":
        #                 continue
        #             if board[row][col]  in seen:
        #                 return False
        #             seen.add(board[row][col])

        # return True
        



        #optimized


        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if (board[i][j] in rows[i] or
                    board[i][j] in cols[j] or
                    board[i][j] in square[i//3, j//3]):

                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                square[i//3, j//3].add(board[i][j])

        return True
