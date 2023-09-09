from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []

        def calculate(lOper, rOper, op):
            if op == "+":
                return lOper + rOper
            elif op == "-":
                return lOper - rOper
            elif op == "*":
                return lOper * rOper
            else:
                return int(lOper/rOper)
        
        for token in tokens:
            if token not in ops:
                stack.append(token)
            else:
                rOper = stack.pop()
                lOper = stack.pop()

                rOper = int(rOper)
                lOper = int(lOper)

                az = calculate(lOper, rOper, token)

                az = str(az)

                stack.append(az)

        return int(stack[0])


if __name__ == "__main__":
    (testcase1, ans1) = (["2","1","+","3","*"], 9)
    (testcase2, ans2) = (["4","13","5","/","+"], 6)
    (testcase3, ans3) = (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22)
    
    sol = Solution()
    assert sol.evalRPN(testcase1) == ans1, "Testcase 1 failed"
    assert sol.evalRPN(testcase2) == ans2, "Testcase 2 failed"
    assert sol.evalRPN(testcase3) == ans3, "Testcase 3 failed"

    print("All test cases passed Pass")