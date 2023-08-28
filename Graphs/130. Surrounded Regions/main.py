from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> List[List[str]]:
        R, C = len(board), len(board[0])
        def dfs(x, y):
            R, C = len(board), len(board[0])
            if 0 <= x < R and 0 <= y < C and board[x][y] == "O":
                board[x][y] = "#"
                neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                for nei in neighbors:
                    dfs(x+nei[0], y+nei[1])

        for i in range(R):
            dfs(i, 0)
            dfs(i, C-1)

        for j in range(C):
            dfs(0, j)
            dfs(R-1, j)

        for i in range(R):
            for j in range(C):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

        return board

if __name__ == "__main__":
    (testcase1, ans1) = ([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]], [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]])
    (testcase2, ans2) = ([["O","X","O","O","O","O","O","O","O"],["O","O","O","X","O","O","O","O","X"],["O","X","O","X","O","O","O","O","X"],["O","O","O","O","X","O","O","O","O"],["X","O","O","O","O","O","O","O","X"],["X","X","O","O","X","O","X","O","X"],["O","O","O","X","O","O","O","O","O"],["O","O","O","X","O","O","O","O","O"],["O","O","O","O","O","X","X","O","O"]], [["O","X","O","O","O","O","O","O","O"],["O","O","O","X","O","O","O","O","X"],["O","X","O","X","O","O","O","O","X"],["O","O","O","O","X","O","O","O","O"],["X","O","O","O","O","O","O","O","X"],["X","X","O","O","X","O","X","O","X"],["O","O","O","X","O","O","O","O","O"],["O","O","O","X","O","O","O","O","O"],["O","O","O","O","O","X","X","O","O"]])
    (testcase3, ans3) = ([["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]], [["X","O","X","O","X","O"],["O","X","X","X","X","X"],["X","X","X","X","X","O"],["O","X","O","X","O","X"]])
    
    sol = Solution()
    assert sol.solve(testcase1) == ans1, "Testcase 1 failed"
    assert sol.solve(testcase2) == ans2, "Testcase 2 failed"
    assert sol.solve(testcase3) == ans3, "Testcase 3 failed"

    print("All test cases passed Pass")

