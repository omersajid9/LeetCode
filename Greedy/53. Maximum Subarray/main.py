from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSum = max(curSum, maxSum)

        return maxSum


if __name__ == "__main__":
    (testcase1, ans1) = ([-2,1,-3,4,-1,2,1,-5,4], 6)
    (testcase2, ans2) = ([5,4,-1,7,8] , 23)
    
    sol = Solution()
    assert sol.maxSubArray(testcase1) == ans1, "Testcase 1 failed"
    assert sol.maxSubArray(testcase2) == ans2, "Testcase 2 failed"

    print("All test cases passed Pass")

