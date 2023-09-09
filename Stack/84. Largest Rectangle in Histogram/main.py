from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        monoS = []
        maxi = 0

        for index, height in enumerate(heights):
            if not monoS:
                monoS.append((index, height))
            else:
                l_ind = -1
                while monoS and monoS[-1][1] > height:
                    l_ind, l_hei = monoS.pop()
                    maxi = max(maxi, (index-l_ind)*l_hei)
                if l_ind > 0:
                    monoS.append((l_ind, height))
                else:
                    monoS.append((index, height))

        while monoS:
            l_ind, l_hei = monoS.pop()
            maxi = max(maxi, (len(heights)-l_ind)*l_hei)
        
        return maxi



if __name__ == "__main__":
    (testcase1, ans1) = ([2,1,5,6,2,3], 10)
    (testcase2, ans2) = ([2,4], 4)
    
    sol = Solution()
    assert sol.largestRectangleArea(testcase1) == ans1, "Testcase 1 failed"
    assert sol.largestRectangleArea(testcase2) == ans2, "Testcase 2 failed"

    print("All test cases passed Pass")