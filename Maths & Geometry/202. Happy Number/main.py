class Solution:
    def isHappy(self, n: int) -> bool:
        memo = {}        

        def getNextNum(n):
            str_n = str(n)
            num = 0
            for s_n in str_n:
                num += int(s_n) * int(s_n)
            return num


        while n not in memo and n != 1:
            memo[n] = True
            n = getNextNum(n)

        return True if n == 1 else False
    
if __name__ == "__main__":
    (testcase1, ans1) = (19, True)
    (testcase2, ans2) = (2, False)
    
    sol = Solution()
    assert sol.isHappy(testcase1) == ans1, "Testcase 1 failed"
    assert sol.isHappy(testcase2) == ans2, "Testcase 2 failed"

    print("All test cases passed Pass")