from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        #Visited set
        visited = set()

        totalNotRotten = 0

        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    totalNotRotten += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ind = 0
        rott = 0
        while q:
            lenQ = len(q)
            isRott = False
            for i in range(lenQ):
                orang = q.popleft()
                for nei in neighbors:
                    new_orang = (orang[0] + nei[0], orang[1] + nei[1])
                    if 0 <= new_orang[0] < len(grid) and 0 <= new_orang[1] < len(grid[0]) and new_orang not in visited and grid[new_orang[0]][new_orang[1]] == 1:
                        q.append(new_orang)
                        visited.add(new_orang)
                        isRott = True
                        rott += 1
            if isRott:
                ind += 1
        
        if totalNotRotten != rott:
            return -1

        return ind

if __name__ == "__main__":
    (testcase1, ans1) = ([[2,1,1],[1,1,0],[0,1,1]], 4)
    (testcase2, ans2) = ([[2,1,1],[0,1,1],[1,0,1]] , -1)
    (testcase3, ans3) = ([[0,2]] , 0)
    
    
    sol = Solution()
    assert sol.orangesRotting(testcase1) == ans1, "Testcase 1 failed"
    assert sol.orangesRotting(testcase2) == ans2, "Testcase 2 failed"
    assert sol.orangesRotting(testcase3) == ans3, "Testcase 3 failed"

    print("All test cases passed Pass")
