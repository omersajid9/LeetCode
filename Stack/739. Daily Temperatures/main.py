from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempLen = len(temperatures)

        monoS = []
        ans = [0] * tempLen

        for i in range(tempLen - 1, -1, -1):
            while monoS and temperatures[monoS[-1]] <= temperatures[i]:
                monoS.pop()
            if monoS:
                ans[i] = monoS[-1] - i
            monoS.append(i)
        return ans

if __name__ == "__main__":
    (testcase1, ans1) = ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0])
    (testcase2, ans2) = ([30,40,50,60], [1,1,1,0])
    (testcase3, ans3) = ([30,60,90], [1,1,0])
    
    sol = Solution()
    assert sol.dailyTemperatures(testcase1) == ans1, "Testcase 1 failed"
    print("==Executed==")
    assert sol.dailyTemperatures(testcase2) == ans2, "Testcase 2 failed"
    print("==Executed==")
    assert sol.dailyTemperatures(testcase3) == ans3, "Testcase 3 failed"
    print("==Executed==")

    print("All test cases passed Pass")