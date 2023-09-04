from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(goal, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

if __name__ == "__main__":
    (testcase1, ans1) = ([2,3,1,1,4], True)
    (testcase2, ans2) = ([3,2,1,0,4] , False)
    
    sol = Solution()
    assert sol.canJump(testcase1) == ans1, "Testcase 1 failed"
    assert sol.canJump(testcase2) == ans2, "Testcase 2 failed"

    print("All test cases passed Pass")
