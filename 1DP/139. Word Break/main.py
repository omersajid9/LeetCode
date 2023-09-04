from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def dfs(string):
            if string in memo:
                return memo[string]

            if string == "":
                return True

            for i in range(len(string)+1):
                if string[:i] in wordDict:
                    if dfs(string[i:]):
                        memo[string] = True
                        return True
            
            memo[string] = False
        ans = dfs(s)
        return ans if ans else False

if __name__ == "__main__":
    (testcase1, ans1) = (["leetcode", ["leet", "code"]], True)
    (testcase2, ans2) = (["applepenapple", ["apple", "pen"]] , True)
    (testcase3, ans3) = (["catsandog", ["cats", "dog", "sand", "and", "cat"]] , False)

    sol = Solution()
    assert sol.wordBreak(testcase1[0], testcase1[1]) == ans1, "Testcase 1 failed"
    assert sol.wordBreak(testcase2[0], testcase2[1]) == ans2, "Testcase 2 failed"
    assert sol.wordBreak(testcase3[0], testcase3[1]) == ans3, "Testcase 3 failed"

    print("All test cases passed Pass")
