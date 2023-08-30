class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        index1 = 0
        index2 = 0

        result = ""
        
        while index1 < len(word1) or index2 < len(word2):

            char1 = word1[index1] if index1 < len(word1) else ""
            char2 = word2[index2] if index2 < len(word2) else ""

            result += char1 + char2

            index1 += 1
            index2 += 1

        return result

if __name__ == "__main__":
    (testcase1, ans1) = (["abc", "pqr"], "apbqcr")
    (testcase2, ans2) = (["ab", "pqrs"], "apbqrs")
    (testcase3, ans3) = (["abcd", "pq"], "apbqcd")
    
    sol = Solution()
    assert sol.mergeAlternately(testcase1[0], testcase1[1]) == ans1, "Testcase 1 failed"
    assert sol.mergeAlternately(testcase2[0], testcase2[1]) == ans2, "Testcase 2 failed"
    assert sol.mergeAlternately(testcase3[0], testcase3[1]) == ans3, "Testcase 3 failed"

    print("All test cases passed Pass")

