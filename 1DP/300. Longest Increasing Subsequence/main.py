from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * length

        dp[-1] = 1

        for i in range(length - 1, - 1, - 1):
            for j in range(i, length):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+  dp[j])
        return max(dp)
    
if __name__ == "__main__":
    (testcase1, ans1) = ([10,9,2,5,3,7,101,18], 4)
    (testcase2, ans2) = ([0,1,0,3,2,3], 4)
    (testcase3, ans3) = ([7,7,7,7,7,7,7], 1)
    
    sol = Solution()
    assert sol.lengthOfLIS(testcase1) == ans1, "Testcase 1 failed"
    assert sol.lengthOfLIS(testcase2) == ans2, "Testcase 2 failed"
    assert sol.lengthOfLIS(testcase3) == ans3, "Testcase 3 failed"

    print("All test cases passed")