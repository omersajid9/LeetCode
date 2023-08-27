class Solution:
    def answer(self, s: str) -> int:
        length = len(s)
        dp = [0] * (length+1)
        
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, length+1):
            if 0 < int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[length]


        # for i in range(length - 1, -1, -1):
        #     if s[i] == '0':
        #         dp[i] = 0
        #     else:
        #         dp[i] = dp[i+1]

        #     if (i + 1 < length and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456'))):
        #         dp[i] += dp[i+2]
        
        # return dp[0]



if __name__ == "__main__":
    (testcase1, ans1) = ("12", 2)
    (testcase2, ans2) = ("226", 3)
    (testcase3, ans3) = ("06", 0)
    (testcase4, ans4) = ("10", 1)
    (testcase5, ans5) = ("2101", 1)
    (testcase6, ans6) = ("1201234", 3)
    
    sol = Solution()
    assert sol.answer(testcase1) == ans1, "Testcase 1 failed"
    assert sol.answer(testcase2) == ans2, "Testcase 2 failed"
    assert sol.answer(testcase3) == ans3, "Testcase 3 failed"
    assert sol.answer(testcase4) == ans4, "Testcase 4 failed"
    assert sol.answer(testcase5) == ans5, "Testcase 5 failed"
    assert sol.answer(testcase6) == ans6, "Testcase 6 failed"

    print("All test cases passed passed")

