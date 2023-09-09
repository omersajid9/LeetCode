from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        monoS = []

        z = zip(position, speed)
        z = sorted(z, key=lambda a: a[0])

        for p, s in z:
            eta = (target-p)/s
            while monoS and monoS[-1] <= eta:
                monoS.pop()
            monoS.append(eta)

        return len(monoS)

        




if __name__ == "__main__":
    (testcase1, ans1) = ([12, [10,8,0,5,3], [2,4,1,1,3]], 3)
    (testcase2, ans2) = ([10, [3], [3]], 1)
    (testcase3, ans3) = ([100, [0,2,4], [4,2,1]], 1)
    
    sol = Solution()
    assert sol.carFleet(*testcase1) == ans1, "Testcase 1 failed"
    print("==Executed==")
    assert sol.carFleet(*testcase2) == ans2, "Testcase 2 failed"
    print("==Executed==")
    assert sol.carFleet(*testcase3) == ans3, "Testcase 3 failed"
    print("==Executed==")

    print("All test cases passed Pass")