from typing import List
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses

        adjacent = collections.defaultdict(list)
        
        for (course, prereq) in prerequisites:
            indegrees[course] += 1
            adjacent[prereq].append(course)

        cycle = True
        for i in indegrees:
            if i == 0:
                cycle = False
        if cycle == True:
            return False

        q = collections.deque()
        res = []

        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)

        while q:
            curCourse = q.popleft()
            res.append(curCourse)
            for nei in adjacent[curCourse]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
                

        return len(res) == numCourses
        
if __name__ == "__main__":
    (testcase1, ans1) = ([2, [[0, 1]]], True)
    (testcase2, ans2) = ([2, [[1,0],[0,1]]] , False)
    (testcase3, ans3) = ([20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]] , False)
    
    sol = Solution()
    assert sol.canFinish(testcase1[0], testcase1[1]) == ans1, "Testcase 1 failed"
    assert sol.canFinish(testcase2[0], testcase2[1]) == ans2, "Testcase 2 failed"
    assert sol.canFinish(testcase3[0], testcase3[1]) == ans3, "Testcase 3 failed"

    print("All test cases passed Pass")
