class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, 1+n):
            if n % i == 0:
                k -= 1
            if k == 0:
                return i
        return  -1
    
if __name__ == "__main__":
    (testcase1, ans1) = ([12, 3], 3)
    (testcase2, ans2) = ([7, 2], 7)
    
    sol = Solution()
    assert sol.kthFactor(*testcase1) == ans1, "Testcase 1 failed"
    assert sol.kthFactor(*testcase2) == ans2, "Testcase 2 failed"

    print("All test cases passed Pass")