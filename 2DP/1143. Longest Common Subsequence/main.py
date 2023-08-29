from typing import List
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)

        dp = [[0 for _ in range(len1+1)] for _ in range(len2+1)]

        for j in range(1, 1+len1):
            for i in range(1, 1+len2):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return dp[len2][len1]

if __name__ == "__main__":
    (testcase1, ans1) = (["abcde", "ace"], 3)
    (testcase2, ans2) = (["abc", "abc"] , 3)
    (testcase3, ans3) = (["abc", "def"] , 0)
    (testcase4, ans4) = (["bsbininm", "jmjkbkjkv"] , 1)
    
    sol = Solution()
    assert sol.longestCommonSubsequence(testcase1[0], testcase1[1]) == ans1, "Testcase 1 failed"
    assert sol.longestCommonSubsequence(testcase2[0], testcase2[1]) == ans2, "Testcase 2 failed"
    assert sol.longestCommonSubsequence(testcase3[0], testcase3[1]) == ans3, "Testcase 3 failed"
    assert sol.longestCommonSubsequence(testcase4[0], testcase4[1]) == ans4, "Testcase 4 failed"

    print("All test cases passed Pass")
