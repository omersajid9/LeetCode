from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        preqDic = defaultdict(list)

        if not prerequisites:
            return list(range(numCourses))
            
        for course, preq in prerequisites:
            indegrees[course] += 1
            preqDic[preq].append(course)

        q = []
        for ind in range(numCourses):
            if indegrees[ind] == 0:
                q.append(ind)
        if not q:
            return q

        res = []
        while q:
            cur = q.pop()
            res.append(cur)
            for nei in preqDic[cur]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)

        return res

if __name__ == "__main__":
    (testcase1, ans1) = ([2, [[1, 0]]], [0, 1])
    (testcase2, ans2) = ([4, [[1,0],[2,0],[3,1],[3,2]]] , [0, 2, 1, 3])
    (testcase3, ans3) = ([1, []] , [0])
    (testcase4, ans4) = ([3, [[1, 0]]] , [2, 0, 1])
    
    sol = Solution()
    assert sol.findOrder(testcase1[0], testcase1[1]) == ans1, "Testcase 1 failed"
    assert sol.findOrder(testcase2[0], testcase2[1]) == ans2, "Testcase 2 failed"
    assert sol.findOrder(testcase3[0], testcase3[1]) == ans3, "Testcase 3 failed"
    assert sol.findOrder(testcase4[0], testcase4[1]) == ans4, "Testcase 4 failed"

    print("All test cases passed Pass")

