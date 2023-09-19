from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        size = len(citations)
        currMax = 0

        for i, c in enumerate(citations):
            if c <= (size-i):
                currMax = c
            else:
                currMax = max(currMax, size-i)
        return currMax
        

if __name__ == "__main__":
    (testcase1, ans1) = ([3,0,6,1,5], 3)
    (testcase2, ans2) = ([1,3,1], 1)
    
    sol = Solution()
    assert sol.hIndex(testcase1) == ans1, "Testcase 1 failed"
    assert sol.hIndex(testcase2) == ans2, "Testcase 2 failed"

    print("All test cases passed Pass")