from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs(x, y, preVal, dic):
            if 0 <= x < len(heights) and 0 <= y < len(heights[0]) and heights[x][y] >= preVal and (x, y) not in dic:
                dic.add((x, y))
                neighbors = [(0, 1), (0, -1), (-1, 0), (1, 0)]
                for nei in neighbors:
                    dfs(x+nei[0], y+nei[1], heights[x][y], dic)

        R, C = len(heights), len(heights[0])

        pac = set()
        alt = set()
        for i in range(R):
            dfs(i, 0, 0, pac)
            dfs(i, C-1, 0, alt)

        for j in range(C):
            dfs(0, j, 0, pac)
            dfs(R-1, j, 0, alt)

        res = []
        for val in pac:
            if val in alt:
                res.append([val[0], val[1]])
        return res

if __name__ == "__main__":
    (testcase1, ans1) = ([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]], [[0,4],[4,0],[3,1],[1,4],[3,0],[2,2],[1,3]])
    (testcase2, ans2) = ([[1]] , [[0,0]])
    
    sol = Solution()
    assert sol.pacificAtlantic(testcase1) == ans1, "Testcase 1 failed"
    assert sol.pacificAtlantic(testcase2) == ans2, "Testcase 2 failed"

    print("All test cases passed Pass")
