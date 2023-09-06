from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(nums, target, index, curSum):
            if (index, curSum) in memo:
                return memo[(index, curSum)]
            if index >= len(nums) and curSum == target:
                return 1
            if index >= len(nums) and curSum != target:
                return 0
            
            posi = backtrack(nums, target, index+1, curSum + nums[index])
            negi = backtrack(nums, target, index+1, curSum - nums[index])

            memo[(index, curSum)] = posi + negi
            return memo[(index, curSum)]

        return backtrack(nums, target, 0, 0)
    
if __name__ == "__main__":
    (testcase1, ans1) = ([[1,1,1,1,1], 3], 5)
    (testcase2, ans2) = ([[1], 1], 1)
    
    sol = Solution()
    assert sol.findTargetSumWays(testcase1[0], testcase1[1]) == ans1, "Testcase 1 failed"
    assert sol.findTargetSumWays(testcase2[0], testcase2[1]) == ans2, "Testcase 2 failed"

    print("All test cases passed")