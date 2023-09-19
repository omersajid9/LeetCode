class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []

        def isSpace(char):
            return char == " " or char == ""


        left = 0
        right = 1

        while isSpace(s[left]):
            left += 1
            right += 1

        while right < len(s):
            if isSpace(s[right]):
                if not isSpace(s[left:right]):
                    stack.append(s[left:right])
                left = right + 1

            right += 1
        if left != right:
            stack.append(s[left:right])

        return " ".join(stack[::-1])
            
if __name__ == "__main__":
    (testcase1, ans1) = ("the sky is blue", "blue is sky the")
    (testcase2, ans2) = ("  hello world  ", "world hello")
    (testcase3, ans3) = ("  a good  example  ", "example good a")
    
    sol = Solution()
    assert sol.reverseWords(testcase1) == ans1, "Testcase 1 failed"
    assert sol.reverseWords(testcase2) == ans2, "Testcase 2 failed"
    assert sol.reverseWords(testcase3) == ans3, "Testcase 3 failed"

    print("All test cases passed Pass")